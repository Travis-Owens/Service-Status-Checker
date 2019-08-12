# Build queue
# for service in self.services:
#
#     # "Switch" method for mapping service type
#     protocols = {
#         'http': check_http,
#         'ping': check_ping,
#         'smtp': check_smtp,
#         'dns' : check_dns,
#     }
#
#     method = protocols[service['service_type']]
#
#     thread_args = [method, service]
#     # t = Thread(target = method(service).check)
#     # t.deamon = True
#     self.queue.put(thread_args)
#
# while(active_count() <= self.thread_limit and not self.queue.empty()):
#     t = self.queue.get()
#     t.start()
#     print("active_count: " + str(active_count()))
