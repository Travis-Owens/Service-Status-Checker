#author: Mathisco-01
#date: 8/16/2019


import pymysql

import config as CONFIG


def create_connection():
		db_config = CONFIG.DB_CONFIG

		try:
			connection = pymysql.connect(host=db_config["DB_HOST"],
							 user=db_config["DB_USER"],
							 password=db_config["DB_PASS"],
							 database=db_config["DB_DATABASE"],
							 charset='utf8mb4',
							 cursorclass=pymysql.cursors.DictCursor)

			return connection
		except Exception as e:
			return str(e)