import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    version = "0.1.0"
    title = "love me sexy"

    app_settings = {
        'db_name': "mymongo",
        'mongodb_url': os.getenv('MONGO_URL'),
        'db_username': os.getenv('MONGO_USER'),
        'db_password': os.getenv('MONGO_PASSWORD'),
        'max_db_conn_count': os.getenv('MAX_CONNECTIONS_COUNT'),
        'min_db_conn_count': os.getenv('MIN_CONNECTIONS_COUNT'),
    }

