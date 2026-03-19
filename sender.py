from cryptography.fernet import Fernet

# Generate key (temporary)
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt(data):
    return cipher.encrypt(data)

def decrypt(data):
    return cipher.decrypt(data)

print(key)  # this will show your key