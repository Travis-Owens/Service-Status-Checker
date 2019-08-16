#Author: @Travis-Owens
#Date: 2019-8-7
#Description: This manages database entries, along with sending notifications

from modules.notification_manager import notification_manager

class service_status_manager(object):
    def __init__(self):
        pass

    def event(self, service, current_status):
        print("event: " + str(service['url']) + " " + str(current_status))
        if(service['last_checked_status'] == current_status):
            # No change, send no alerts
            return

        if(current_status == False):
            # Service is now offline
            self.send_alert(service, False)

        if(current_status == True):
            # Service is now online
            self.send_alert(service, True)

        self.db_update_status(service, current_status)


    def send_alert(self, service, status):

        # Set message string
        if(status == True):
            message = str(service['service_name'] + " is now Online.")

        if(status == False):
            message = str(service['service_name'] + " is now Offline.")

        # Send email
        if(service['notification_email'] == True):
            notification_manager().send_email(service['email'], message)

        # Send SMS
        if(service['notification_sms'] == True):
            notification_manager().send_sms(service['phone_number'], message)


    def db_update_status(self, service, status):
        pass
