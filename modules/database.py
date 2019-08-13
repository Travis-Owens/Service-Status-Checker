# Author: @Travis-Owens
# Date:   2019-7-31

import pymysql

class database(object):
	def __init__(self):
		pass

	def create_connection(self, db_config):
		try:
			connection = pymysql.connect(host=db_config["DB_HOST"],
							 user=db_config["DB_USER"],
							 password=db_config["DB_PASS"],
							 database=db_config["DB_DATABASE"],
							 charset='utf8mb4',
							 cursorclass=pymysql.cursors.DictCursor)

			return connection

		except Exception as e:
			print(e)
			print("Can't fetch service database. Stopping ...")
			exit()

		

	def create_table(self, connection):
		with connection.cursor() as cursor:
			try:
				cursor.execute("CREATE TABLE services (service_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, service_created TIMESTAMP DEFAULT now(), last_updated TIMESTAMP DEFAULT now() ON UPDATE now(), service_name TEXT, service_type TEXT, service_address TEXT, last_checked_status BOOLEAN, notification_email BOOLEAN, notification_sms BOOLEAN, email TEXT, phone_number TEXT)")
				connection.commit()
				print("Table succesfully created!")

			except pymysql.MySQLError as e:
				if("(1050," in str(e)): #1050 is warning code for table allready exists
					print("Found table!")
				else:
					print(e)

			except Exception as e:
				print(e)
				
	def get_services(self, queue, db_config):

		print("Attempting to connect to: '{}' at: '{}' as: '{}'".format(db_config["DB_DATABASE"], db_config["DB_HOST"], db_config['DB_USER']))
		connection = self.create_connection(db_config)
		print("Connected!")

		#Create tables if not exist, we run this every time just to be safe
		self.create_table(connection)


		# TODO: Implement DB fetch here, columns should be placed stored as a dict
		services = [
				{'service_id':1, 'service_name': 'google.com', 'service_type':'http', 'address':'http://google.com', 'last_checked_status': True, 'notification_email' : True, 'notification_sms': True, 'email': 'g@t.com', 'phone_number': '44444'},
		]

		for service in services:
			queue.put(service)
