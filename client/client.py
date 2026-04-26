import socket
import struct
import time
from cryptography.fernet import Fernet
from crypto.pqc_utils import generate_hmac

ATTACK_MODE = False   # change to True to simulate attack

def send_data(sock, data):
    length = struct.pack('!I', len(data))
    sock.sendall(length + data)

client = socket.socket()
client.connect(('localhost', 9999))

# Session key generation
session_key = Fernet.generate_key()
cipher = Fernet(session_key)

send_data(client, session_key)

print("✅ Secure session established\n")

while True:
    msg = input("Send any message : ")

    if msg.lower() == "exit":
        break

    start_time = time.time()

    # ================= FILE MODE =================
    if msg.startswith("/file"):
        filename = msg.split(" ")[1]

        with open(filename, "rb") as f:
            data = f.read()

        encrypted_data = cipher.encrypt(data)

        # 🔥 Attack simulation
        if ATTACK_MODE:
            encrypted_data = encrypted_data[:-5] + b'abc'

        hmac_val = generate_hmac(session_key, encrypted_data)

        send_data(client, b"FILE")
        send_data(client, filename.encode())
        send_data(client, encrypted_data)
        send_data(client, hmac_val.encode())

        end_time = time.time()

        print("\n📁 FILE TRANSFER")
        print("File Name:", filename)
        print("Encrypted Size:", len(encrypted_data))
        print("HMAC:", hmac_val)
        print("Time Taken:", round(end_time - start_time, 4), "sec\n")

        continue

    # ================= MESSAGE MODE =================
    encrypted_msg = cipher.encrypt(msg.encode())

    # 🔥 Attack simulation
    if ATTACK_MODE:
        encrypted_msg = encrypted_msg[:-5] + b'xyz'

    hmac_val = generate_hmac(session_key, encrypted_msg)

    send_data(client, b"MSG")
    send_data(client, encrypted_msg)
    send_data(client, hmac_val.encode())

    end_time = time.time()

    # 🔥 PRINT (VERY IMPORTANT FOR REPORT)
    print("\n🔐 MESSAGE SENT")
    print("Original Message:", msg)
    print("Encrypted Message:", encrypted_msg.decode())
    print("HMAC:", hmac_val)
    print("Time Taken:", round(end_time - start_time, 4), "sec\n")

client.close()