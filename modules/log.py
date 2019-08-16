#author: Mathisco-01
#date: 08/16/2019

import os
import pymysql
import time

import config as CONFIG
import modules.db_connection as db_connection

class logging(object):

	def __init__(self):

		self.db_config = CONFIG.DB_CONFIG

		self.temp_connection = db_connection.create_connection()
		if(type(self.temp_connection) == type("travis big gay")):

			self.log_error_locally(self.temp_connection) #self.temp_connection is now a string because it returned an error.
			e = "COULD NOT ESTABLISH CONNECTION TO DATABASE. PLEASE CHECK config.py !STOPPING ..."
			self.log_error_locally(e)
			print(e)
			exit()

	def log_error_locally(self, error_message):
		if(os.path.exists("errorlog.txt") == True):
			with open("errorlog.txt", "a+") as f:
				error_message = str(time.strftime("%b %d %Y %H:%M:%S", time.gmtime(time.time()))) + "	" + str(error_message) + "\n"
				f.write(error_message)
				f.close()
		else:
			try:
				f = open("errorlog.txt", "w+")
				f.close()
				self.log_error_locally(error_message)

			except Exception as e:
				#this is really the end all be all for shitty exceptions. it means that everything so far has failed. prob check if your internet is working or somethign.
				print("Could not log error locally!")
				print(e)

	def log_error(self, error_message):
		print(error_message)	

		with self.temp_connection.cursor() as cursor:
			try:
				#log the error locally
				self.log_error_locally(error_message)

				#log the error in the database
				cursor.execute("""INSERT INTO exceptions (exception) VALUES ("%s")""" % (error_message))
				self.temp_connection.commit()
				print("succesfully logged exception in database")

			except Exception as e:
				#log error message locally
				self.log_error_locally(error_message)

				#log why couldn't write to database locally
				self.log_error_locally(e)

				print("!! Could not log exception!!")

