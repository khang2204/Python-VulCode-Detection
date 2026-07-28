import mysql.connector
import os
import time
import datetime
import calendar
import hashlib
import sys
import argparse
db = mysql.connector.connect(host='localhost', user='root', passwd='root',
    db='elixir', buffered=True)
cur = db.cursor()
def get_file_size(path):...
"""docstring"""
return os.path.getsize(path)
