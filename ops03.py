#!/usr/bin/env python3

# Author: Jansen Lefever
# Class: 401D2 Ops Challenge 3
# Purpose: Email failed connection alert 

import smtplib, os, time, datetime

fromaddr = '***********@gmail.com'  
toaddrs  = '***********@gmail.com'   

username = '********'  
password = '********'

addr = input("What Ip Address would you like to ping:" )

now = datetime.datetime.now()
ping = os.system("ping -c 1 " + str(addr))

def email_up():
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    (server.login(username, password))

    msg = "Network connection to" + str(addr) + " " + "is back up \n"
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

def email_down():
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    (server.login(username, password))

    msg = "Network connection to" + str(addr) + " " + "is down \n"
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

while True:
        print()
        time.sleep( 1 )
        if ping == 0:
            print((str(now)) + " " + "Network Active to " + str(addr))
        if ping != 0:
            print((str(now)) + " " + "Connection Failed to " + str(addr))
            email_down()
            if ping == 0:
                print((str(now)) + " " + "Network Active to " + str(addr))
                email_up()
        time.sleep( 1 )
