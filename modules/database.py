# Author: @Travis-Owens
# Date:   2019-7-31

import pymysql

class database(object):
    def __init__(self):
        pass

    def get_services(self, queue):
        # TODO: MySQL integration


        # TODO: Implement DB fetch here
        services = [
                {'service_id':1, 'service_name': 'google.com', 'service_type':'http', 'url':'http://google.com', 'last_checked_status': True, 'notification_email' : True, 'notification_sms': True, 'email': 'g@t.com', 'phone_number': '44444'},
        ]

        for service in services:
            queue.put(service)
