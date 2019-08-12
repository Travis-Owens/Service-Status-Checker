#Author: @Travis-Owens
#Date: 2019-8-7
#Description: sends email and SMS.


class notification_manager(object):
    def __init__(self):
        pass

    def send_email(self, email, message):
        print('sending email to: ' + str(email))
        print('message: ' + str(message))
        print()
        return

    def send_sms(self, phone_number, message):
        print('sending sms to: ' + str(phone_number))
        print('message: ' + str(message))
        print()
        return
