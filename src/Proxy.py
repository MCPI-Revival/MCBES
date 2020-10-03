# this file is part of the mcbes project
#   _  _   ___  ____  ____      ____ 
#  ( \/ ) / __)(  _ \(  __)___ / ___)
#  / \/ \( (__  ) _ ( ) _)(___)\___ \
#  \_)(_/ \___)(____/(____)    (____/

import time
import os
# TODO: Import RakPy

from utils import logger, fs
from utils.Utils import Utils

from wizard import wizard

from lang import base

logo = """
    _  _   ___  ____  ____      ____ 
   ( \/ ) / __)(  _ \(  __)___ / ___)
   / \/ \( (__  ) _ ( ) _)(___)\___ \

   \_)(_/ \___)(____/(____)    (____/
   """


class Proxy:
    def __init__(self, path, withWizard, isTravisBuild = False):
        super().__init__()
        self.path = path
        self.withWizard = withWizard
        if(withWizard):
            fs.checkAllFiles(path)
        else:
            wizard.skipWizard(path)
        port = 19132
        print(str(logo))
        wizard.isInWizard = False
        logger.log('info',  str(base.get("startingServer")).replace("{ip}", str(Utils.getPrivateIpAddr())).replace("{port}", str(port)))
        logger.log('info', str(base.get("extIpMsg")).replace("{ipPublic}", str(Utils.getPublicIpAddr())))
        logger.log('info', str(base.get("license")))
        server = PyRakLibServer(port=19132)
        handler = ServerHandler(server, None)
        handler.sendOption("name", "MCPE; MCBES Proxy;390;1.14.60;0;0;0;MCBES Proxy;0")
        if (isTravisBuild):
            print("Build success.")
            os._exit(0)
        else:
            while wizard.isInWizard == False:
                cmd = input('> ')
                command(cmd, True)
                cmd = None
            ticking = True
            while ticking:
                time.sleep(0.002)


def command(string, fromConsole):
    if string.lower() == 'stop':
        logger.log('info', 'Stopping proxy...')
        Utils.killServer()
    elif string.lower() == '':
        pass
    elif string.lower() == 'help':
        logger.log('info', '/stop: Stops the proxy')
    else:
        logger.log('error', str(base.get("invalidCommand")))
