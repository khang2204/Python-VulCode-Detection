import sqlite3
import os
from server.settings import BASE_DIR
DB_FILE = os.path.join(BASE_DIR, 'db.sqlite3')
def sqlite_executor(sql):...
conn = sqlite3.connect(DB_FILE)
sql = 'select * from django_migrations;'
cursor = conn.cursor()
cursor.execute(sql)
res = cursor.fetchall()
return res
