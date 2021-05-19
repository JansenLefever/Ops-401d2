#! /usr/bin/env python3

import os, hashlib

def linux():
    fil = input("Name a file: \n")
    dirs = input("Name a Directory: \n")
    os.system(f"ls {dirs}")
    os.system(f"find {dirs} -name {fil}")
    md5_hash = hashlib.md5()
    with open(fil,"rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            md5_hash.update(byte_block)
        print(md5_hash.hexdigest())
    

def windows():
    fil = input("Name a file: \n")
    dirs = input("Name a Directory: \n")
    os.system(f"dir Images /AD /b /s {dirs} \\ {fil}").read()
    with open(fil,"rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            md5_hash.update(byte_block)
        print(md5_hash.hexdigest())    

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