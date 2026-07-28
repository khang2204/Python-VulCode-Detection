import os
import calendar
from datetime import datetime, timedelta
from itertools import groupby
from collections import Counter
from functools import wraps
from tools.failures import SETA_WINDOW
from src import jobtypes
import MySQLdb
from flask import Flask, request, json, Response, abort
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
static_path = os.path.join(os.path.dirname(SCRIPT_DIR), 'static')
app = Flask(__name__, static_url_path='', static_folder=static_path)
JOBSDATA = jobtypes.Treecodes()
def __init__(self, cset_id):...
self.cset_id = cset_id
self.green = Counter()
self.orange = Counter()
self.red = Counter()
self.blue = Counter()
def create_db_connnection():...
return MySQLdb.connect(host='localhost', user='root', passwd='root', db='ouija'
    )
