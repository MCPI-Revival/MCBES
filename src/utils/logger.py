# this file is part of the mcbes project
#   _  _   ___  ____  ____      ____ 
#  ( \/ ) / __)(  _ \(  __)___ / ___)
#  / \/ \( (__  ) _ ( ) _)(___)\___ \
#  \_)(_/ \___)(____/(____)    (____/

from datetime import datetime
from .TextFormat import TextFormat


TextFormat = TextFormat()


def log(type_, content):
    time = datetime.now()
    if type_ == 'info':
        print(f'{TextFormat.BLUE}[INFO: {time.strftime("%H:%M")}]{TextFormat.WHITE} {content}')
    elif type_ == 'warn':
        print(f'{TextFormat.YELLOW}[WARNING: {time.strftime("%H:%M")}]{TextFormat.WHITE} {content}')
    elif type_ == 'error':
        print(f'{TextFormat.RED}[ERROR: {time.strftime("%H:%M")}]{TextFormat.WHITE} {content}')
    elif type_ == 'success':
        print(f'{TextFormat.GREEN}[SUCCESS: {time.strftime("%H:%M")}]{TextFormat.WHITE} {content}')
    elif type_ == "emergency":
    	print(f'{TextFormat.GOLD}[EMERGENCY: {time.strftime("%H:%M")}]{TextFormat.WHITE} {content}')
    elif type_ == "alert":
    	print(f'{TextFormat.PURPLE}[ALERT: {time.strftime("%H:%M")}]{TextFormat.WHITE} {content}')
    elif type_ == "notice":
    	print(f'{TextFormat.AQUA}[NOTICE: {time.strftime("%H:%M")}]{TextFormat.WHITE} {content}')
    elif type_ == "critical":
        print(f'{TextFormat.RED}[CRITICAL: {time.strftime("%H:%M")}]{TextFormat.WHITE} {content}')
    elif type_ == "debug":
        print(f'{TextFormat.GRAY}[DEBUG: {time.strftime("%H:%M")}]{TextFormat.WHITE} {content}')
    else:
        print(f'[{type_.upper()}: {time.strftime("%H:%M")}]{content}')
