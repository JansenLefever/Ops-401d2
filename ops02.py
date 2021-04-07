#!/usr/bin/env python3

import os, time, datetime

addr = input("What Ip Address would you like to ping:" )

now = datetime.datetime.now()
ping = os.system("ping -c 1 " + str(addr))

while True:
        print()
        time.sleep( 1 )
        if ping == 0:
            print((str(now)) + " " + "Network Active to " + str(addr))
        else:
            print((str(now)) + " " + "Connection Failed to " + str(addr))
        time.sleep( 1 )

