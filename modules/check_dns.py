# Author: @Travis-Owens
# Date:   2019-7-31

# External Import
from socket import gethostbyname

# Internal Imports
from modules.log import logging
from modules.service_status_manager import service_status_manager as ssm

class check_dns(object):
    def __init__(self, service):
        self.service = service

    def check(self):
        try:
            # gethostbyname does not work with the prefix http or https
            if( self.service['service_address'].startswith('http://') ):
                hostname = self.service['service_address'][7:]
            elif( self.service['service_address'].startswith('https://') ):
                hostname = self.service['service_address'][8:]
            else:
                hostname = self.service['service_address']

            # Attempt to resolve hostname
            query = gethostbyname(hostname)

            # If gethostbyname is unable to resolve the domain to an IP it will
            # trigger the exception below, if the script reaches this point
            # the status is True
            status = True

        except socket.gaierror as e:
            # unable to reslove hostname to an IP
            status = False

        except Exception as e:
            logging().log_error(e)

        # Initialize service_status_manager
            ssm().event(self.service, status)

        return
