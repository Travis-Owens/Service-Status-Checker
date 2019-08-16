# Author: @Travis-Owens
# Co-Author: @Mathisco-01
# Date:   2019-7-31

import pymysql
import os
import time

import config as CONFIG
from modules.log import logging
import modules.db_connection as db_connection

class database(object):

	def __init__(self):

		self.db_config = CONFIG.DB_CONFIG
		self.services = []
		self.logging = logging()

		print("Attempting to connect to: '{}' at: '{}' as: '{}'".format(self.db_config["DB_DATABASE"], self.db_config["DB_HOST"], self.db_config['DB_USER']))
		self.connection = db_connection.create_connection()

	def create_exceptions_table(self):
		with self.connection.cursor() as cursor:
			try:
				cursor.execute("CREATE TABLE exceptions (log_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, exception TEXT, timestamp TIMESTAMP DEFAULT now() ON UPDATE now())")
				self.connection.commit()
				return True

			except pymysql.MySQLError as e:
				if("1050" in str(e)): #1050 is warning code for table allready exists
					return True
				else:
					return e

			except Exception as e:
				return e

	def create_services_table(self,):
		with self.connection.cursor() as cursor:
			try:
				cursor.execute("CREATE TABLE services (service_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, service_created TIMESTAMP DEFAULT now(), last_updated TIMESTAMP DEFAULT now() ON UPDATE now(), service_name TEXT, service_type TEXT, service_address TEXT, last_checked_status BOOLEAN, notification_email BOOLEAN, notification_sms BOOLEAN, email TEXT, phone_number TEXT)")
				self.connection.commit()
				return True

			except pymysql.MySQLError as e:
				if("1050" in str(e)): #1050 is warning code for table allready exists
					return True
				else:
					return e

			except Exception as e:
				return e

	def fetch_services(self):
		with self.connection.cursor() as cursor:
			try:
				cursor.execute("SELECT * FROM services")
				rows = cursor.fetchall()
			except Exception as e:
				self.logging.log_error(e)

			if(len(rows) > 0):
				for service in rows:
					self.services.append(service)

				print("Found {} services in: '{}' at: '{}'".format(len(self.services), self.db_config["DB_DATABASE"], self.db_config["DB_HOST"]))

			else:
				e = "No services in database! Stopping ..."
				self.logging.log_error(e)
				exit()


	def get_services(self, queue):

		#Create tables if not exist, we run this every time just to be safe
		#Correct response: tables = [True, True]
		tables =[self.create_exceptions_table(), self.create_services_table()]
		if(tables != [True, True]):
			if(tables[0] != True):
				print("Exceptions table could not be found nor be created!")
				self.logging.append(e)
			if(tables[1] != True):
				print("Services table could not be found nor created!")
				self.logging.append(e)

		#fetches all services form DB and adds it to self.services
		self.fetch_services()

		for service in self.services:
			queue.put(service)

		return queue

