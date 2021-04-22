#!/usr/bin/env python3

import ipaddress
from scapy.all import ICMP, IP, sr1, TCP

# Define end host and TCP port range. Take care not to populate the host bits here.
def ip_scan():
    network = input("Enter a network address (Include CIDR block): ")
    ip_list = ipaddress.ip_network(network)
    hosts_scanned = 0
    hosts_count = 0
    hosts_block = 0

    for host in ip_list:
        print("Pinging ",host,", please wait...")
        response = sr1(
            IP(dst=str(host))/ICMP(),
            timeout=.01,
            verbose=0
    )
        if response is None:
            print (f"{host} is down")
            hosts_scanned+=1
        elif response.haslayer(ICMP):
            hosts_scanned+=1
            hosts_count+=1
            if (int(response.getlayer(ICMP).type) == 3 and
                int(response.getlayer(ICMP).code) [1,2,3,9,10,13]):
                hosts_block+=1
                print (f"{host} is blocking ICMP traffic")
            else:
                print(f"{host} is up. Total hosts online: {hosts_count}")
        else:
            print(f"{hosts_scanned} ip addresses scanned.")
            print(f"{hosts_count} hosts are up;")
            print(f"{hosts_block} are blocking ICMP traffic.")

ip_scan()