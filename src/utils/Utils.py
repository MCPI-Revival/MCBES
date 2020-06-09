# this file is part of the mcbes project
#   _  _   ___  ____  ____      ____ 
#  ( \/ ) / __)(  _ \(  __)___ / ___)
#  / \/ \( (__  ) _ ( ) _)(___)\___ \
#  \_)(_/ \___)(____/(____)    (____/

import sys
import os
import signal
import socket
import urllib

class Utils:

    def getOS():
        if sys.platform == 'linux' or sys.platform == 'linux2':
            return 'linux'
        elif sys.platform == 'darwin':
            return 'osx'
        elif sys.platform == 'win32' or sys.platform == 'win64':
            return 'windows'
        
    def killServer():
        os.kill(os.getpid(), signal.SIGTERM)
    
    def getPrivateIpAddr():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    
    def getPublicIpAddr():
        ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        return ip
