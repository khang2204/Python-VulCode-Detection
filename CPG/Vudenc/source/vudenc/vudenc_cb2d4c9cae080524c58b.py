from datetime import datetime
from os.path import exists
from sqlite3 import connect
from termcolor import colored
from threading import Lock
from traceback import format_exc, format_stack
log_exception = '__LOG_EXCEPTION__'
log_trace = '__LOG_TRACE__'
def __init__(self, campaign={}, create_result=False, database_file=...
if not exists(database_file):
self.campaign = campaign
self.result = {}
self.file = database_file
self.lock = Lock()
if create_result:
db.__create_result()
def __enter__(self):...
def dict_factory(cursor, row):...
dictionary = {}
for id_, column in enumerate(cursor.description):
dictionary[column[0]] = row[id_]
return dictionary
