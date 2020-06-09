# this file is part of the mcbes project
#   _  _   ___  ____  ____      ____ 
#  ( \/ ) / __)(  _ \(  __)___ / ___)
#  / \/ \( (__  ) _ ( ) _)(___)\___ \
#  \_)(_/ \___)(____/(____)    (____/

from lang import base
import os

def checkYesNo(string):
    string = string.lower()
    if string == 'y' or string == 'yes':
        return True
    elif string == 'n' or string == 'no':
        return False
    else:
        return

def checkIfLangExists(string):
    path = os.getcwd() + '/src/Podrum/lang/'
    allLangs = base.getLangNames(path)
    if(string in allLangs):
        return True
    else:
        return False
