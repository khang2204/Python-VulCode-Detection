import sqlite3
import os.path
from cpwrap import CFG
import random
import string
def connectDB():...
conn = sqlite3.connect(CFG('dbname'))
return conn, conn.cursor()
