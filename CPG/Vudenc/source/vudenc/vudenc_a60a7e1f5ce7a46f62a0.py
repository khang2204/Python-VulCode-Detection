import os
import sqlite3
import utils
from os import path
from utils import SQLiteUtils
getSQLiteType = SQLiteUtils.getSQLiteType
from threading import Lock
from textual_data import DATABASES_FOLDER_NAME, METADATA_FILENAME
SCRIPT_FOLDER = path.dirname(path.realpath(__file__))
TABLE_NAME = 'files'
def __init__(self, filename):...
"""docstring"""
super(FileDB, self).__init__()
os.makedirs(path.join(SCRIPT_FOLDER, DATABASES_FOLDER_NAME), exist_ok=True)
self.filename = path.join(SCRIPT_FOLDER, DATABASES_FOLDER_NAME, filename +
    '.db')
self.lock = Lock()
initial = {'type': 0, 'meta': 'str', 'path': 'str', 'mod_time': 0,
    'file_id': 'str'}
if initial:
if path.isfile(self.filename):
def getDBFilename(self):...
for i in initial.keys():
self.createTable(initial)
"""docstring"""
self._addColumn(i, initial[i])
return self.filename
