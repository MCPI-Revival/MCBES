#!/usr/bin/env python3

# this file is part of the mcbes project
#   _  _   ___  ____  ____      ____ 
#  ( \/ ) / __)(  _ \(  __)___ / ___)
#  / \/ \( (__  ) _ ( ) _)(___)\___ \
#  \_)(_/ \___)(____/(____)    (____/

import sys
from os import getcwd
from threading import Thread
from Proxy import Proxy

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        if sys.argv[1] == "--no_wizard" and sys.argv[2] == "-travis":
                serverThread = Thread(target=Proxy, args=(getcwd(), False, True))
        else:
            print("[!] None valid args selected.")
            serverThread = Thread(target=Proxy, args=(getcwd(), True))
    elif len(sys.argv) == 2:
        if sys.argv[1] == "--no_wizard":
                serverThread = Thread(target=Proxy, args=(getcwd(), False))
        else:
            print("[!] None valid args selected.")
            serverThread = Thread(target=Proxy, args=(getcwd(), True))
    else:
        serverThread = Thread(target=Proxy, args=(getcwd(), True))
    serverThread.start()
