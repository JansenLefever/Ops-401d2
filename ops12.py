#!/usr/bin/env python3

import ipaddress
from scapy.all import ICMP, IP, sr1, TCP

# Define end host and TCP port range. Take care not to populate the host bits here.

network = "192.168.1.0/24"
ip_list = ipaddress.ip_network(network)
hosts_count = 0

for host in ip_list:
    print("Pinging ",host,", please wait...")
    response = sr1(
        IP(dst=str(host))/ICMP(),
        timeout=.01,
        verbose=0
    )

print(response)