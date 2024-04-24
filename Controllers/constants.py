import util.configFile as conf

config = conf.init()

CONTENT_TYPE = "application/json"

SECRET_KEY = "cherry"

# API PORT configurations
API_HOST = config.get('SERVER', 'host')
API_PORT = config.get('SERVER', 'port')
DEBUG = config.get('SERVER', 'debug')

# JSON SCHEMA PATH FOR SEND
REGISTER_SCHEMA = config.get('JSON_PATH', 'register_schema')
LOGIN_SCHEMA = config.get('JSON_PATH', 'login_schema')
LEAVE_SCHEMA = config.get('JSON_PATH', 'leave_schema')
ADD_EMPLOYEE = config.get('JSON_PATH', 'add_employee')

# DATABASE CONFIGURATIONS
DB_USER = config.get('DATABASE', 'db_user')
DB_PASSWORD = config.get('DATABASE', 'db_password')
DB_HOST = config.get('DATABASE', 'db_host')
DB_PORT = config.get('DATABASE', 'db_port')
DB_NAME = config.get('DATABASE', 'db_database')

LEAVE_TYPES = ['earned_leave', 'sick_leave', 'bereavement_leave']

# ERROR RESPONSES
INVALID_CREDENTIALS = {
    "status_code": "401",
    "error_code": "E101",
    "error_message": "Invalid Credentials",
    "data": 'Please enter the valid credentials for verification'
}

INVALID_JSON = {
                "status_code": "400",
                "error_code": "E101",
                "error_message": "Invalid JSON format"
            }
