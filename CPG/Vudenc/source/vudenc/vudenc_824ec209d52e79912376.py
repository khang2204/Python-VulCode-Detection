def sqlite_executor(sql):...
conn = sqlite3.connect(DB_FILE)
sql = 'select * from django_migrations;'
cursor = conn.cursor()
cursor.execute(sql)
res = cursor.fetchall()
return res
