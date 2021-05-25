#! /usr/bin/env python3

import os

target = input("Please enter an IP or URL \n:")
port_range = input("Please enter a port range \n:")

print("")
print(f"Starting Netcat scan of {target}. \n")
os.system(f"nc -z -v {target} {port_range} 2>&1 | grep succeeded")
print("")
print(f"Starting Telnet Connection of {target}. \n")
os.system(f"telnet -b {target} port {port_range}")
print("")
print(f"Starting Nmap scan of {target}. \n")
os.system(f"nmap {target} -p {port_range}")