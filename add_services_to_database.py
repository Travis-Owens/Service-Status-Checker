#author: @Mathisco-01
#date:	 2019-8-13

import pymysql

import config as CONFIG
from modules.database   import database

class main(object):
	def __init__(self):
		self.db_config = CONFIG.DB_CONFIG

		#print(self.db_config)
		self.connection = database().create_connection(self.db_config)


	def insert_new_service(self, iv): #iv stands for insert_values. It's shortened to keep the code below relatively short.
		with self.connection.cursor() as cursor:
			try:
				sql = """INSERT INTO services (service_name, service_type, service_address, last_checked_status, notification_email, notification_sms, email, phone_number)
						VALUES ("%s","%s","%s","%s","%s","%s","%s","%s")""" % (iv["service_name"], iv["service_type"], iv["service_address"], int(iv["last_checked_status"]), int(iv["notification_email"]), int(iv["notification_sms"]), iv["email"], iv["phone_number"])

				#cursor.execute(self.connection.escape_string(sql))
				cursor.execute(sql)
				self.connection.commit()
			except Exception as e:
				print(e)

	def YN_checker(self, string):
		if("y" in string.lower()):
			return True
		else:
			return False


	def run(self):
		iv = {}

		iv["service_name"] = 		input("Service name: ")
		iv["service_type"] = 		input("Service type: ")
		iv["service_address"] = 	input("Service address (URL): ")
		iv["last_checked_status"] = self.YN_checker(input("Last checked status (Y/n): "))
		iv["notification_email"] =  self.YN_checker(input("Recieve email notifications (Y/n): "))
		iv["notification_sms"] = 	self.YN_checker(input("Recieve sms notifications (Y/n): "))
		iv["email"] = 				input("Email address: ")
		iv["phone_number"] = 		input("Phone number: ")

		print("Are you sure you want to insert {} this into: '{}' at: '{}' as: '{}'".format(iv, self.db_config["DB_DATABASE"], self.db_config["DB_HOST"], self.db_config['DB_USER']))
		if(self.YN_checker(input("Y/n: ")) == True):
			self.insert_new_service(iv)
		else:
			print("Stopping ...")
			exit()

if __name__ == "__main__":
	main().run()
