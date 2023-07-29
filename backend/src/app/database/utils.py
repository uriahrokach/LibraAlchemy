from server.utils.config import get_config
from .models import db

import os


def connect_to_db():
    """
    Connects to the mongodb database using the configuration connection string
    """
    conn_str = get_config().db.connection
    username = os.environ.get("MONGO_USERNAME")
    password = os.environ.get("MONGO_PASSWORD")

    db.connect(username=username, password=password, host=conn_str)
