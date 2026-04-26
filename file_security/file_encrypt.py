from cryptography.fernet import Fernet

def encrypt_file(filename):
    key = Fernet.generate_key()
    cipher = Fernet(key)

    with open(filename, "rb") as f:
        data = f.read()

    encrypted = cipher.encrypt(data)

    with open("encrypted_" + filename, "wb") as f:
        f.write(encrypted)

    return key