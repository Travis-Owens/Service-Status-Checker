# Author: @Travis-Owens
# Co-Author: @Mathisco-01
# Date:   2019-7-31

import pymysql

class database(object):

	def __init__(self):

		self.services = []

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
			print("COULD NOT ESTABLISH CONNECTION TO DATABASE. PLEASE CHECK config.py !STOPPING ...")
			print(e)
			exit()

	def create_exceptions_table(self, connection):
		with connection.cursor() as cursor:
			try:
				cursor.execute("CREATE TABLE exceptions (log_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, exception TEXT, timestamp TIMESTAMP DEFAULT now() ON UPDATE now())")
				connection.commit()
				print("Table 'exceptions' succesfully created!")

			except pymysql.MySQLError as e:
				if("1050" in str(e)): #1050 is warning code for table allready exists
					print("Found 'exceptions' table!")
				else:
					print("COULD NOT ESTABLISH CONNECTION TO 'EXCEPTIONS' DATABSE! REASON:")
					print(e)

			except Exception as e:
				print("COULD NOT ESTABLISH CONNECTION TO 'EXCEPTIONS' DATABSE! REASON:")
				print(e)	

	def create_services_table(self, connection):
		with connection.cursor() as cursor:
			try:
				cursor.execute("CREATE TABLE services (service_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, service_created TIMESTAMP DEFAULT now(), last_updated TIMESTAMP DEFAULT now() ON UPDATE now(), service_name TEXT, service_type TEXT, service_address TEXT, last_checked_status BOOLEAN, notification_email BOOLEAN, notification_sms BOOLEAN, email TEXT, phone_number TEXT)")
				connection.commit()
				print("Table 'services' succesfully created!")

			except pymysql.MySQLError as e:
				if("1050" in str(e)): #1050 is warning code for table allready exists
					print("Found 'services' table!")
				else:
					print(e)

			except Exception as e:
				print(e)

	def fetch_services(self, connection):
		with connection.cursor() as cursor:
			try:
				cursor.execute("SELECT * FROM services")
				rows = cursor.fetchall()
			except Exception as e:
				print(e)

			if(len(rows) > 0):
				for service in rows:
					self.services.append(service)

				print("Found {} services!".format(len(self.services)))

			else:
				print("No services in database! Stopping ...")
				exit()

	def log_error(self, error_message):
		temp_connection = self.connection

		with temp_connection.cursor() as cursor:
			try:
				cursor.execute("""INSERT INTO exceptions (exception) VALUES ("%s")""" % (error_message))
				temp_connection.commit()
				print("succesfully logged exception in database")
			except Exception as e:
				print(e)
				print("!! Could not log exception!!")
				#have to write exception log file thing in here		


	def get_services(self, queue, db_config):

		print("Attempting to connect to: '{}' at: '{}' as: '{}'".format(db_config["DB_DATABASE"], db_config["DB_HOST"], db_config['DB_USER']))
		self.connection = self.create_connection(db_config)
		print("Connected to database!")

		#Create tables if not exist, we run this every time just to be safe
		self.create_exceptions_table(self.connection)
		self.create_services_table(self.connection)

		self.log_error("peepeepoopoo test123")

		#fetches all services form DB and adds it to self.services
		self.fetch_services(self.connection)

		for service in self.services:
			queue.put(service)
