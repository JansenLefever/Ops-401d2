#!/usr/bin/env python3

# Author: Jansen Lefever
# Class: 401D2 Ops Challenge 2
# Purpose: Checking uptime

import os, time, datetime

addr = input("What Ip Address would you like to ping:" )

now = datetime.datetime.now()
ping = os.system("ping -c 1 " + str(addr))

while True:
        print ("Start Ping attempt : %s" % time.ctime())
        print()
        time.sleep( 1 )
        if ping == 0:
            print(str(now))
            print("Network Active to " + str(addr))
        else:
            print("Connection Failed " + str(now))
        print()
        print ("End Ping attempt : %s" % time.ctime())
        print()
        time.sleep( 1 )

