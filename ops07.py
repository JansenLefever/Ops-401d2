#!/usr/bin/env python3

# Author: Jansen Lefever
# Class: 401D2 Ops Challenge 7
# Purpose: 

from cryptography.fernet import Fernet, os

def load_key():
    # Load the key from the current directory named `key.key`
    return open("key.key", "rb").read()

def Encrypt_file():
    f = Fernet(key)
    
    with open(filepath, "rb") as directory:
        file_data = directory.read()
    Enc_file = f.encrypt(file_data)

    with open(filepath, "wb") as file:
        file.write(Enc_file)

key = load_key()
filepath = input("Enter File path \n>:")

def Encrypt_dir():
#    f = Fernet(key)
    
# Begin recursive directory crawl
    for root, dirs, files in os.walk(filepath, topdown=False):
# For each hit, concatenate the current directory pathing to left of result
        for name in files:
            datapath = (os.path.join(root, name))
            f = Fernet(key)
    
    with open(datapath, "rb") as directory:
        file_data = directory.read()
    Enc_file = f.encrypt(file_data)

    with open(datapath, "wb") as file:
        file.write(Enc_file)
        for name in dirs:
            print(os.path.join(root, name))
            Encrypt_file()
           
    

Encrypt_dir()

