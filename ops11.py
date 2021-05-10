#! /usr/bin/env python3

# Run this with sudo

import random

from scapy.all import ICMP, IP, sr1, TCP

# Define target host and TCP port to scan
host= "scanme.nmap.org"
port_range= "22, 23, 80, 443. 3389" 

for dst_port in port_range:
    src_port=(random.randint(4000,6500))
    response = sr1(IP(dst=(host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0)

    if response is None:
        print(f"{host}:{dst_port} is filtered")

    elif(response.haslayer(TCP)):
        if(response.getlayer(TCP).flags == 0x12):
            send_rst = sr(IP(dst=(host))/TCP(sport=src_port,dport=dst_port,flags="R"),timeout=1,verbose=0)
        
            print(f"{host}:{dst_port} is open")

    elif(response.getlayer(TCP).flags == 0x14):
        print(f"{host}:{dst_port} is closed")

    elif(response.haslayer(ICMP)):
        if(
            int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]
        ):
            print(f"{host}:{dst_port} is filtered")


# https://ladderpython.com/lesson/random-module-in-python-3-generate-random-number-in-python-3/