#Author: @Travis-Owens
#Co-Author: @Mathisco-01
#Date: 2019-8-7
#Description: sends email and SMS.

import config as CONFIG
import modules.log as logging

from twilio.rest import Client


class notification_manager(object):
    def __init__(self):

        self.logging = logging()


        #Twilio config
        self.twilio_phone_number = CONFIG.twilio_phone_number
        self.twilio_account_sid = CONFIG.twilio_account_sid
        self.twilio_auth_token = CONFIG.twilio_auth_token
        self.client = Client(self.twilio_account_sid, self.twilio_auth_token)


        #Email config
        self.email_send_as = CONFIG.email_send_as

    def send_email(self, email, message):
        print('sending email to: ' + str(email))
        print('message: ' + str(message))
        print()
        return

    def send_sms(self, phone_number, message):
        print('sending sms to: ' + str(phone_number))
        print('message: ' + str(message))
        

        try:
            message = client.messages.create(
                            body=str(message),
                            from_=self.twilio_phone_number,
                            to=str(phone_number))
        except Exception as e:
            self.logging.log_error(e)


        return


#For testing
if __name__ == "__main__":
    nm = notification_manager()
    nm.send_sms("", "travis big gay")