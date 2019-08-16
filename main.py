# Author: @Travis-Owens
# Date:   2019-7-31

# External Imports
from threading import Thread
from threading import active_count
from multiprocessing import Queue

# Local Imports
import config as CONFIG
from modules.database   import database
from modules.log import logging

from modules.check_http import check_http
from modules.check_ping import check_ping
from modules.check_smtp import check_smtp
from modules.check_dns  import check_dns


class main(object):
    def __init__(self):

        # Variable used to limit the amount of concurrent threads
        self.thread_limit = CONFIG.thread_limit

        self.queue = Queue()

        #"Switch" method for mapping service type
        self.protocols = {
            'http'  : check_http,
            'https' : check_http,
            'ping'  : check_ping,
            'smtp'  : check_smtp,
            'dns'   : check_dns,
        }

        self.db_config = CONFIG.DB_CONFIG

        self.logging = logging()

    def run(self):

        database().get_services(self.queue, self.db_config)         # Fetches services from MySQL database

        self.thread_limit += int(active_count())    # Exlude runtime threads from the thread limit count

        # Loop while the queue is not empty
        while(not self.queue.empty()):

            # concurrent thread limiting
            if(active_count() <= self.thread_limit):

                service = self.queue.get()                          # Get service dict from the queue
                method  = self.protocols[service['service_type']]   # "Switch" select the required function

                # Create thread and start it, pass the service dict to the object
                t = Thread(target = method(service).check)
                t.deamon = True
                t.start()
        return

if __name__ == "__main__":
    main().run()
