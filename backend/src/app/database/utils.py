from ..server.utils.config import get_config
from .models import db


def connect_to_db():
    """
    Connects to the mongodb database using the configuration connection string
    """
    conn_str = get_config()['DB_CONFIG']
    db.connect(host=conn_str)
