# this file is part of the mcbes project
#   _  _   ___  ____  ____      ____ 
#  ( \/ ) / __)(  _ \(  __)___ / ___)
#  / \/ \( (__  ) _ ( ) _)(___)\___ \
#  \_)(_/ \___)(____/(____)    (____/

import os
import glob
import json
from wizard import wizard
from utils import TextFormat

"""
 getLangFiles and getLangNames are 
 for the wizard's use
"""

langsList = [0]

def getLangFiles(dir):
    path = dir + '/src/lang'
    allFiles = glob.glob(path + '/*.json')
    for file in allFiles:
        with open(f'{file}', 'r', encoding="utf8") as langFiles:
            data = json.load(langFiles)
            if "langName" in data:
                name = data['langName']
            else:
                name = 'Unknown name'
        langs = str(file.replace(path, '').replace("\\", "").replace('.json', ''))
        langsList.append(langs)
        print(f'[{langs}] -> {name}')

def getLangNames(dir):
    return langsList

"""
A translation from the selected 
language is returned
"""
def get(string):
    if wizard.isInWizard == True:
        path = os.getcwd() + "/src/lang/"
        with open(f'{path}/{wizard.options[0]}.json', 'r', encoding="utf8") as lF:
            data = json.load(lF)
            if string in data:
                return data[string]
            else:
                print(f"The value '{string}' does not exists in this language.")
    else:
        serverConfig = os.getcwd() + "/proxy.json"
        with open(f'{serverConfig}', 'r', encoding="utf8") as serverCfg:
            pref = json.load(serverCfg)
            if "Language" in pref:
                lang = pref["Language"]
            else:
                print(f"{TextFormat.RED}Language not found in proxy.json")
        path = os.getcwd() + "/src/lang/"
        with open(f'{path}{lang}.json', 'r', encoding="utf8") as lF:
            data = json.load(lF)
            if string in data:
                return data[string]
            else:
                print(f"{TextFormat.RED}The value '{string}' does not exists in this language.")
