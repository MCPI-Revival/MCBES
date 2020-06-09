# this file is part of the mcbes project
#   _  _   ___  ____  ____      ____ 
#  ( \/ ) / __)(  _ \(  __)___ / ___)
#  / \/ \( (__  ) _ ( ) _)(___)\___ \
#  \_)(_/ \___)(____/(____)    (____/

import os
import json
from wizard import wizard


def read(file):
    with open(file) as f:
        return f.read()
        f.close()


def write(file, content):
    with open(file) as f:
        f.write(content)
        f.close()


# Name include extension
def createFile(path, name):
    f = open(f'{path}/{name}', 'w+')
    f.close()


def createDir(path, name):
    try:
        os.mkdir(f'{path}/{name}')
    except:
        pass


def checkForFile(path, name):
    return os.path.isfile(f'{path}/{name}')


def checkForDir(path):
    return os.path.isdir(f'{path}')


def checkAllFiles(path):
    firstLaunch = False
    if not checkForFile(path, 'proxy.json') or (os.path.getsize(f'{path}/proxy.json') == 0):
        createFile(path, 'proxy.json')
        firstLaunch = True
    elif not checkForFile(path, 'plugins'):
        createDir(path, 'plugins')
    if firstLaunch:
        wizard.wizard(path)

def createServerConfigFromWizard(path, isWizardSkipped, options):
    if(isWizardSkipped == False):
        with open(f'{path}/proxy.json', 'w', encoding="utf8") as file:
            content = {
            "MOTD": options[1],
            "Language": options[0],
            "MaxPlayers": options[2]

            }
            json.dump(content, file, indent=4, skipkeys=True, ensure_ascii=False)
    else:
        content = {
            "MOTD": "MCBES Proxy",
            "Language": "en",
            "MaxPlayers": "20"

        }
        with open(f'{path}/proxy.json', 'w', encoding="utf8") as fl:
            json.dump(content, fl, indent=4, skipkeys=True)
