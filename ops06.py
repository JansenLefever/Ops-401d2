#!/usr/bin/env python3

# Author: Jansen Lefever
# Class: 401D2 Ops Challenge 6
# Purpose: 

# Encrypt a single string

# Import Libraries

from cryptography.fernet import Fernet

# Declare Functions

def write_key():
    # Generate a key and save it into a file
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    # Load the key from the current directory named `key.key`
    return open("key.key", "rb").read()

def Encrpt_string():
    key = load_key()
    print("Key is "+str(key.decode('utf-8')))

    message = "hello friend".encode()
    print("Plaintext is "+str(message.decode('utf-8')))

    # Initialize the Fernet class
    f = Fernet(key)

# Encrypt the message
    encrypted = f.encrypt(message)

# Print how it looks
print(encrypted.decode('utf-8'))

# Main

x = int(input('1)Encrpt Files 2)Decrypt Files 3)Encrypt String 4)Decrypt String 5)Exit'))
    
    
if x == 1:
   
    else:
        print("exiting")
elif x == 2:
    y = str(input("Are you sure? y/n: "))
    if y == 'y':
        response = requests.post(str(site))
        if response.status_code == 200:
            print('Success')
        elif response.status_code == 404:
            print('Site not found')
        else:
            print(response.status_code)
    else:
        print("exiting")
elif x == 3:
    y = str(input("Are you sure? y/n: "))
    if y == 'y':
        response = requests.put(str(site))
        if response.status_code == 200:
            print('Success')
        elif response.status_code == 404:
            print('Site not found')
        else:
            print(response.status_code)
    else:
        print("exiting")
elif x == 4:
    y = str(input("Are you sure? y/n: "))
    if y == 'y':
        response = requests.delete(str(site))
        if response.status_code == 200:
            print('Success')
        elif response.status_code == 404:
            print('Site not found')
        else:
            print(response.status_code)
    else:
        print("exiting")
elif x == 5:
    y = str(input("Are you sure? y/n: "))
    if y == 'y':
        response = requests.head(str(site))
        if response.status_code == 200:
            print('Success')
        elif response.status_code == 404:
            print('Site not found')
        else:
            print(response.status_code)
    else:
        print("exiting")
  

# Generate and write a new key
#write_key()

# load the previously generated key


