#!/usr/bin/env python3

import ipaddress
from scapy.all import ICMP, IP, sr1, TCP

# Define end host and TCP port range. Take care not to populate the host bits here.

network = input("Enter a network address (Include CIDR block): ")
ip_list = ipaddress.ip_network(network)
hosts_count = 0

for host in ip_list:
    print("Pinging ",host,", please wait...")
    response = sr1(
        IP(dst=str(host))/ICMP(),
        timeout=.01,
        verbose=0
    )
    if(int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]):
        print(f"{host}: is blocking ICMP traffic")

print(response)