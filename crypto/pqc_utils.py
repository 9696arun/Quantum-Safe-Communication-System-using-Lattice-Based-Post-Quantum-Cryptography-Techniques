from cryptography.fernet import Fernet
import hmac
import hashlib
import os

# -------------------------------
# Simulated PQC Key Generation
# -------------------------------
def generate_keys():
    public_key = os.urandom(32)
    private_key = os.urandom(32)
    return public_key, private_key


# -------------------------------
# Session Key Generator
# -------------------------------
def generate_session_key():
    return Fernet.generate_key()


# -------------------------------
# Encrypt Message (Session-based)
# -------------------------------
def encrypt_message(session_key, message):
    cipher = Fernet(session_key)
    return cipher.encrypt(message)


# -------------------------------
# Decrypt Message
# -------------------------------
def decrypt_message(session_key, encrypted_msg):
    cipher = Fernet(session_key)
    return cipher.decrypt(encrypted_msg)


# -------------------------------
# HMAC Generate (UPDATED 🔥)
# -------------------------------
def generate_hmac(key, data):
    return hmac.new(key, data, hashlib.sha256).hexdigest()


# -------------------------------
# HMAC Verify (UPDATED 🔥)
# -------------------------------
def verify_hmac(key, data, received_hmac):
    calc = hmac.new(key, data, hashlib.sha256).hexdigest()
    return calc == received_hmac