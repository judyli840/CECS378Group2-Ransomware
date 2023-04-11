import socket
from cryptography.fernet import Fernet


key = Fernet.generate_key()
with open('thekey.key', 'wb') as key_file:
    key_file.write(key)
with open('key.txt', 'wb') as key_text:
    key_text.write(key)
    print(key)

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

