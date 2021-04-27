#! /usr/bin/env python3
# Import libraries
import time, getpass

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
    while passwd not in line:
        line = line.rstrip()
        line = file.readline()
    
    if passwd in line:
        print(f"\n{passwd} was found in {filepath}.")
            
    else:
        print(f"\n{passwd} wasn't found in {filepath}.")
            
    
     
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
3 - Exit
    Please enter a number: 
""")
        if (mode == "1"):
            iterator()
        elif (mode == "2"):
            check_password()
        elif (mode == '3'):
            break
        else:
            print("Invalid selection...") 