#! /usr/bin/env python3

import random
from scapy.all import ICMP, IP, sr1, TCP

# Define end host and TCP port range
host = "192.168.40.1"
port_range = [22, 23, 80, 443, 3389]

# Send SYN with random Src Port for each Dst port
def port_scan():
    for dst_port in port_range:
    src_port = random.randint(1025,65534)
    resp = sr1(
        IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,
        verbose=0,
    )

    if resp is None:
        print(f"{host}:{dst_port} is filtered (silently dropped).")

    elif(resp.haslayer(TCP)):
        if(resp.getlayer(TCP).flags == 0x12):
            # Send a gratuitous RST to close the connection
            send_rst = sr(
                IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='R'),
                timeout=1,
                verbose=0,
            )
            print(f"{host}:{dst_port} is open.")

        elif (resp.getlayer(TCP).flags == 0x14):
            print(f"{host}:{dst_port} is closed.")

    elif(resp.haslayer(ICMP)):
        if(
            int(resp.getlayer(ICMP).type) == 3 and
            int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
        ):
            print(f"{host}:{dst_port} is filtered (silently dropped).")

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

while True:
    user = input("""
    What would you like to do: 
    (1 Port Scan
    (2 Ping Network
    (3 Exit
    """)
    if (user == "1"):
        port_scan()
     elif (user == "2"):
        ip_scan()
    elif (user == '3'):
        print("Exiting")
        break
    else:
        print("Invalid selection...")
