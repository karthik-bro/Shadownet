from cryptography.fernet import Fernet

# 👉 Paste your copied key here (VERY IMPORTANT)
key = b'VfDP0PEyW3X8-9W-G2C28mzKe3z5QbEg9w0wNdgyVOk='

cipher = Fernet(key)

def encrypt(data):
    return cipher.encrypt(data)

def decrypt(data):
    return cipher.decrypt(data)