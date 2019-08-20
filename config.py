# Configuration Information

# Runtime Variabless
thread_limit = 1

# Database Variables
DB_TYPE = 'MySQL'
DB_HOST = '10.0.0.1'
DB_USER = ''
DB_PASS = ''
DB_DATABASE = 'service-status-checker'

#This exists so we can feed all the database information to database.py alot easier.
DB_CONFIG = {
	"DB_TYPE": DB_TYPE,
	"DB_HOST": DB_HOST,
	"DB_USER": DB_USER,
	"DB_PASS": DB_PASS,
	"DB_DATABASE": DB_DATABASE
}

# Notifcation Variables
twilio_phone_number = ""
twilio_account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
twilio_auth_token = 'your_auth_token'



email_send_as = 'status@status_checker.local'
