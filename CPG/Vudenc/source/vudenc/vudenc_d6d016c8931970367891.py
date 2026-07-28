import pymysql.cursors
from datetime import date, datetime
import json
import config
def __init__(self):...
self.conn = pymysql.connect(user=config.mysql_credentials['user'], password
    =config.mysql_credentials['password'], host=config.mysql_credentials[
    'host'], db=config.mysql_credentials['database'], cursorclass=pymysql.
    cursors.DictCursor)
self.cur = self.conn.cursor()
def __enter__(self):...
return DBase()
