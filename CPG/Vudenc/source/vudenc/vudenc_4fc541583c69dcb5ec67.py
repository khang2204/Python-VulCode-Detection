from time import strftime, time
from pretty_date import prettify_date
import sqlite3
db_name = 'robodb.sqlite'
tb_name = 'robotb'
mapping = 'timestamp INTEGER, name TEXT, location TEXT, description TEXT'
columns = 'timestamp, name, location, description'
one_week = 604800
one_year = 31540000
max_data_length = 70
def __init__(self):...
self.db_name = db_name
self.connection = sqlite3.connect(self.db_name)
def create_table(self):...
stmt = 'CREATE TABLE IF NOT EXISTS {} ({})'.format(tb_name, mapping)
self.connection.execute(stmt)
self.connection.commit()
def insert(self, input_row):...
is_valid, violations = self.validate_row(input_row)
if is_valid:
name, location, description = input_row
return is_valid, violations
date = int(time())
args = date, name, location, description
stmt = 'INSERT INTO {} ({}) VALUES {}'.format(tb_name, columns, str(args))
self.connection.execute(stmt)
self.connection.commit()
