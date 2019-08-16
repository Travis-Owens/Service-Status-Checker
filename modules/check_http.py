# Author: @Travis-Owens
# Date:   2019-7-31
# Description: Returns true if online, and false if offline

import requests
from modules.service_status_manager import service_status_manager as ssm
from modules.log import logging

class check_http(object):
    def __init__(self, service):
        self.service = service
        self.url = service['service_address']

    def check(self):
        try:
            # Try to retrieve webpage and retrieve the returned status code
            request = requests.get(self.url)
            status_code = request.status_code

        except requests.exceptions.ConnectionError as e:
            # This exception triggers when the request lib cannot create a connection to the URL
            ssm().event(self.service, False)
            return

        except Exception as e:
            # Catch all Exception
            logging.log_error(e)

        if(status_code == 200):
            ssm().event(self.service, True)
        else:
            ssm().event(self.service, False)

# Single file-level testing
# if __name__ == "__main__":
#     x = check_http('http://opendata.cf').check()
#     print(x)
