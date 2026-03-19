from encryption.crypto import decrypt
import socket

host = "127.0.0.1"
port = 5001

s = socket.socket()
s.bind((host, port))
s.listen(1)

print("Waiting for connection...")
conn, addr = s.accept()
print("Connected from:", addr)

data = b""
while True:
    chunk = conn.recv(1024)
    if not chunk:
        break
    data += chunk

decrypted_data = decrypt(data)

with open("received_file.txt", "wb") as f:
    f.write(decrypted_data)

print("Decrypted file received successfully!")
conn.close()