import pymysql.cursors
def __init__(self, db):...
connection = pymysql.connect(host='localhost', user='root', password='', db
    =db, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor,
    autocommit=True)
self.connection = connection
def query_db(self, query, data=None):...
query = cursor.mogrify(query, data)
print('Something went wrong', e)
self.connection.close()
def connectToMySQL(db):...
print('Running Query:', query)
return False
return MySQLConnection(db)
executable = cursor.execute(query, data)
if query.lower().find('insert') >= 0:
self.connection.commit()
if query.lower().find('select') >= 0:
return cursor.lastrowid
result = cursor.fetchall()
self.connection.commit()
return result
