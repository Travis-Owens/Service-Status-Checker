# Author: @Travis-Owens
# Date:   2019-7-31
# Description: Returns true if online, and false if offline

import requests
from modules.service_status_manager import service_status_manager as ssm

class check_http(object):
    def __init__(self, service):
        self.service = service
        self.url = service['url']
        pass

    def check(self):
        try:
            r = requests.get(self.url)
            status_code = r.status_code

        except requests.exceptions.ConnectionError as e:
            print("here" + str(e))
            ssm().event(self.service, False)
            return
        except Exception as e:
            print(e)

        if(status_code == 200):
            ssm().event(self.service, True)
        else:
            ssm().event(self.service, False)

# Single file-level testing
# if __name__ == "__main__":
#     x = check_http('http://opendata.cf').check()
#     print(x)
