from cryptography.fernet import Fernet

def decrypt_file(filename, key):
    cipher = Fernet(key)

    with open(filename, "rb") as f:
        data = f.read()

    decrypted = cipher.decrypt(data)

    with open("decrypted_" + filename, "wb") as f:
        f.write(decrypted)