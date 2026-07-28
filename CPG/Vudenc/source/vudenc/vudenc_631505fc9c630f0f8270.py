import pymysql.cursors
def __init__(self, host, user, password, db, charset):...
self.connection = pymysql.connect(host=host, user=user, password=password,
    db=db, charset=charset, cursorclass=pymysql.cursors.DictCursor)
def close_connection(self):...
self.connection.close()
def connect_sql(self, sql):...
"""docstring"""
cursor.execute(sql)
result = cursor.fetchall()
return result
