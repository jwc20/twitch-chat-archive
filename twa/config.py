import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self, instance_path):
        self.FLASK_RUN_PORT = os.getenv('FLASK_RUN_PORT', 5000)
        self.SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'dev')
        self.DB_USER = os.getenv('user'),
        self.DB_PASSWORD = os.getenv('password'),
        self.DB_HOST = os.getenv('host'),
        self.DB_PORT = os.getenv('port'),
        self.DB_NAME = os.getenv('dbname'),
