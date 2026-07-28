"""
Created on Sat Dec 23 13:43:09 2017

@author: Adam
"""
import sys
import os
import time
import warnings
import getpass
import sqlite3
from importlib import import_module
import pymysql
from cryptography.fernet import Fernet
from .core import TABLE, DATA_DIRE, KEY_FILE
from .tools import db_check, db_insert, parse_settings
def get_columns(settings):...
"""docstring"""
sensors = settings['sensors']
if 'column_fmt' in settings:
column_fmt = settings['column_fmt']
columns = ('TIMESTAMP',) + tuple([str(sen).strip() for sen in sensors])
columns = ('TIMESTAMP',) + tuple([column_fmt.replace('{sensor}', str(sen).
    strip()) for sen in sensors])
return columns
