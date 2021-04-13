#!/usr/bin/env python3

# Author: Jansen Lefever
# Class: 401D2 Ops Challenge 6
# Purpose: 

# Encrypt a single string

# Import Libraries

from cryptography.fernet import Fernet, os

# Declare Functions

def write_key():
    # Generate a key and save it into a file
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    # Load the key from the current directory named `key.key`
    return open("key.key", "rb").read()

key = load_key()

def Encrpt_string():
    message = input("What string would you like to encrypt: ")
    mess_e = message.encode()
    f = Fernet(key)
    encrypted = f.encrypt(mess_e)
    print(encrypted.decode('utf-8'))

def Decrypt_string():
    message = input("What string would you like to decrypt: ")
    mess_d = str.encode(message)
    f = Fernet(key)
    decrypted = f.decrypt(mess_d)
    print(decrypted.decode('utf-8'))
   
def Encrypt_file():
    f = Fernet(key)
    filepath = input("Enter File path \n>:")
    with open(filepath, "rb") as file:
        file_data = file.read()
    Enc_file = f.encrypt(file_data)

    with open(filepath, "wb") as file:
        file.write(Enc_file)

def Decrypt_file():
    f = Fernet(key)
    filepath = input("Enter File path \n>:")
    with open(filepath, "rb") as file:
        file_data = file.read()
    Dec_file = f.decrypt(file_data)

    with open(filepath, "wb") as file:
        file.write(Dec_file)

# Main

x = int(input('1)Encrpt String \n2)Decrypt String \n3)Encrypt File \n4)Decrypt File \n5)Exit \nEnter Number: '))
    
if x == 1:
    Encrpt_string()
elif x == 2:
    Decrypt_string()
elif x == 3:
    Encrypt_file()
elif x == 4:
    Decrypt_file()    
elif x == 5:
    print("Exiting")
else:
    print("incorrect input")
  

# Generate and write a new key
#write_key()
# load the previously generated key


