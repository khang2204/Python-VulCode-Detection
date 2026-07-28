import sqlite3
from sqlite3 import Error
import pandas as pd
import sys
import logging
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler(sys.stdout)
log_handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s - line %(lineno)d'
    ))
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)
def create_connection(db_name='cert_db.sqlite3'):...
conn = sqlite3.connect(db_name)
logger.critical(e)
return None
return conn
