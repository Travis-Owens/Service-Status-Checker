# Author: @Travis-Owens
# Date:   2019-7-31

# External Imports
import requests
import pymysql

from threading import Thread
from threading import active_count
from multiprocessing import Queue
from time import sleep

# Local Imports
import config as CONFIG
from modules.database   import database

from modules.check_http import check_http
from modules.check_ping import check_ping
from modules.check_smtp import check_smtp
from modules.check_dns  import check_dns


class main(object):
    def __init__(self):

        self.threads = list()
        self.thread_limit = CONFIG.thread_limit

        self.queue = Queue()

        #"Switch" method for mapping service type
        self.protocols = {
            'http': check_http,
            'ping': check_ping,
            'smtp': check_smtp,
            'dns' : check_dns,
        }

        self.run()

    def run(self):
        self.services = self.get_services()      # Returns a dict with all of the services

        # Build queue # TODO:  Move this to the DB fetch row
        for service in self.services:
            self.queue.put(service)

        sleep(.001)  # queue.put() is non-blocking,this allows for the put opertaions to finish

        self.thread_limit += int(active_count())    # Exlude runtime threads from the thread limit count

        # thread limiting and queue empty checking
        while(not self.queue.empty()):
            if(active_count() <= self.thread_limit):
                service = self.queue.get()
                method  = self.protocols[service['service_type']]

                t = Thread(target = method(service).check)
                t.deamon = True
                t.start()


    def get_services(self):
        # TODO: MySQL integration
        services = [
                {'service_id':1, 'service_name': 'google.com', 'service_type':'http', 'url':'http://google.com', 'last_checked_status': True, 'notification_email' : True, 'notification_sms': True, 'email': 'g@t.com', 'phone_number': '44444'},
        ]

        return services

main()
