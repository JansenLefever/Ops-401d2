#! /usr/bin/env python3

import os

def linux():
    fil = input("Name a file: \n")
    dirs = input("Name a Directory: \n")
    os.system("Find " + (dirs) + "-name " + (fil))
    

def windows():
    fil = input("Name a file: \n")
    dirs = input("Name a Directory: \n")
    os.system("dir Images /AD /b /s" + (dirs) + (fil))

op = input(" 1) Linux 2) Windows 3) Exit \n")

while True:
    if (op == '1'):
        linux()
    elif (op == '2'):
        windows()
    elif (op == '3'):
        break
    else:
        print("Incorrect Input")
