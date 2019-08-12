# Author: @Travis-Owens
# Date:   2019-7-31
# Description: pings server. # TODO: Latency Warning

import subprocess
import platform
import re
class check_ping(object):
    def __init__(self, url):
        self.url = url

    def check(self):

        param = '-n' if platform.system().lower()=='windows' else '-c'
        command = ['ping', param, '1', self.url]

        process = subprocess.call(command, stdout = subprocess.PIPE)
        # process = subprocess.Popen(command, stdout= subprocess.PIPE)
        # print('start')
        # x = str(process.communicate())
        # # print(x)
        # y = x.find("?ms")

        # Latency = x[y+10:]
        # print(Latency)

        if(process == 0):
            print(True)
        else:
            print(False)




# check_ping('144.217.88.111').check()
