#! /usr/bin/env python3

# Run this with sudo

import sys, random

from scapy.all import ICMP, IP, sr1, TCP



# Define target host and TCP port to scan
host=str(input("What host IP would you like to target: "))
port_range=input("What is the port range you want to scan: ")
src_port=(random.randrange(2,4000))
dst_port =input("What would you like your destation port to be: ") 

response = sr1(IP(dst=(host))/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0)

if response== str(0x12):
    print("Sending RST packet. Port is open")
elif response== str(0x14):
    print("This port is closed")
else:
    print("Port is filtered") 

print(response)

# https://ladderpython.com/lesson/random-module-in-python-3-generate-random-number-in-python-3/