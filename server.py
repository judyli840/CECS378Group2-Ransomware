import socket
from cryptography.fernet import Fernet
import os

if os.path.exists('thekey.key'):
    with open('thekey.key', 'rb') as key_file:
        key = key_file.read()
else:
    key = Fernet.generate_key()
    with open('thekey.key', 'wb') as key_file:
        key_file.write(key)   

HOST = socket.gethostname()
IP_ADDRESS = socket.gethostbyname(HOST)
PORT = 9090

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP_ADDRESS, PORT))
server_socket.listen(1)

print(f"Server is listening for incoming connections at: {IP_ADDRESS}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()

    client_socket.sendall(key)
    client_socket.close()
