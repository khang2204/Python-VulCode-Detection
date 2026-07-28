from utils.admin import load_credentials
import MySQLdb
import json
credentials = load_credentials()
dsn = credentials['dbhost'], credentials['dbuser'], credentials['dbpass'
    ], credentials['dbname']
def __init__(self):...
self.conn = MySQLdb.connect(*self.dsn)
self.cur = self.conn.cursor()
def __enter__(self):...
return DBase()
