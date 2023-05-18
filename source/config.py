from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

DB_DRIVER = os.environ.get('DB_DRIVER')
DB_CONNECTOR = os.environ.get('DB_CONNECTOR')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')

DB_DRIVER_TEST = os.environ.get('DB_DRIVER_TEST')
DB_CONNECTOR_TEST = os.environ.get('DB_CONNECTOR_TEST')
DB_USER_TEST = os.environ.get('DB_USER_TEST')
DB_PASS_TEST = os.environ.get('DB_PASS_TEST')
DB_HOST_TEST = os.environ.get('DB_HOST_TEST')
DB_PORT_TEST = os.environ.get('DB_PORT_TEST')
DB_NAME_TEST = os.environ.get('DB_NAME_TEST')

AUTH_SECRET_KEY = os.environ.get('AUTH_SECRET_KEY')
MANAGER_SECRET_KEY = os.environ.get('MANAGER_SECRET_KEY')
EMAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
