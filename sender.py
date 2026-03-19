from encryption.crypto import encrypt
import socket

host = input("Enter receiver IP: ")
port = 5001

s = socket.socket()
s.connect((host, port))

with open("file.txt", "rb") as f:
    data = f.read()
    encrypted_data = encrypt(data)   #  encrypt here
    s.sendall(encrypted_data)

print("Encrypted file sent successfully!")
s.close()