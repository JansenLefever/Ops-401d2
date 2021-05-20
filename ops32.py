#! /usr/bin/env python3

import os, hashlib, time, datetime

def timestamp():
    now = datetime.datetime.now()
    timestamp = now.strftime("%m-%d-%y %H:%M:%S:%f")
    return str(timestamp)

def hash_it(datapath):
    md5_hash = hashlib.md5()
    with open(datapath,"rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            md5_hash.update(byte_block)
        print(md5_hash.hexdigest())
     

def linux():
    filepath = input("Input absolute directory path: \n")
    for root, dirs, files in os.walk(filepath):
    # For each hit, concatenate the current directory pathing to left of result
        for name in files:
            datapath = (os.path.join(root, name))
            time = timestamp()
            print(time)
            hash_it(datapath)
            
    
    
linux()