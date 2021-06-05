#!/usr/bin/python3

import socket
import time

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = time.time() + 20.0
sockmod.settimeout(timeout)

hostip = input("Please provide a host ip address \n:")
portno = input("Enter a port number \n:")

def portScanner(portno):
    try:
        sockmod.connect((hostip, portno))
    except:
        print("Port closed")
        return False
    else:
        print("Port open")
        return True

portScanner(portno)
