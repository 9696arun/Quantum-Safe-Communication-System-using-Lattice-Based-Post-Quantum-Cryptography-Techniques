import socket
import struct
from cryptography.fernet import Fernet
from crypto.pqc_utils import verify_hmac
import csv
import os

# -------------------------------
# Receive Full Data
# -------------------------------
def recv_full(conn, length):
    data = b''
    while len(data) < length:
        packet = conn.recv(length - len(data))
        if not packet:
            return None
        data += packet
    return data

# -------------------------------
# Receive Structured Data
# -------------------------------
def recv_data(conn):
    raw_len = recv_full(conn, 4)
    if not raw_len:
        return None
    length = struct.unpack('!I', raw_len)[0]
    return recv_full(conn, length)

# -------------------------------
# Logging Function (CSV)
# -------------------------------
def log_data(event, size):
    os.makedirs("analysis", exist_ok=True)

    with open("analysis/log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([event, size])

# -------------------------------
# Server Setup
# -------------------------------
server = socket.socket()
server.bind(('localhost', 9999))
server.listen(1)

print("🚀 Server waiting...")

conn, addr = server.accept()
print("✅ Connected:", addr)

# -------------------------------
# Session Key Receive
# -------------------------------
session_key = recv_data(conn)
cipher = Fernet(session_key)

print("🔑 Secure session established\n")

# -------------------------------
# Main Loop
# -------------------------------
while True:
    try:
        msg_type = recv_data(conn)
        if not msg_type:
            break

        # ================= FILE MODE =================
        if msg_type == b"FILE":
            filename = recv_data(conn).decode()
            encrypted_data = recv_data(conn)
            hmac_val = recv_data(conn).decode()   # ✅ FIX

            print("\n📁 Receiving File:", filename)

            if not verify_hmac(session_key, encrypted_data, hmac_val):
                print("❌ File tampered!")
                continue

            data = cipher.decrypt(encrypted_data)

            with open("received_" + filename, "wb") as f:
                f.write(data)

            log_data("FILE", len(data))

            print("✅ HMAC Verified")
            print("📁 File saved as:", "received_" + filename)
            print("📊 File Size:", len(data), "bytes\n")

        # ================= MESSAGE MODE =================
        elif msg_type == b"MSG":
            encrypted_msg = recv_data(conn)
            hmac_val = recv_data(conn).decode()   # ✅ FIX

            print("\n📩 Receiving Message...")

            if not verify_hmac(session_key, encrypted_msg, hmac_val):
                print("❌ Message tampered!")
                continue

            message = cipher.decrypt(encrypted_msg)

            log_data("MSG", len(message))

            print("✅ HMAC Verified")
            print("🔓 Decrypted Message:", message.decode())
            print("📏 Message Size:", len(message), "bytes\n")

    except Exception as e:
        print("⚠️ Error:", e)
        break

# -------------------------------
# Close Connection
# -------------------------------
conn.close()
server.close()
print("🔌 Server closed")