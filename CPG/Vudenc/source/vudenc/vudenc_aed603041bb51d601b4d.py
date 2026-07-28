import psycopg2
from itertools import izip_longest
DBNAME = 'tournament'
def connect():...
"""docstring"""
return psycopg2.connect('dbname=%s' % DBNAME)
