import json
import psycopg2
SQL_INSERT_JSON = "INSERT INTO %s(data) VALUES('%s') RETURNING id"
SQL_QUERY_JSON = 'SELECT %s FROM %s WHERE %s'
SQL_GET_JSON = 'SELECT * FROM %s WHERE id=%s'
def __init__(self, name, connection):...
self.name = name
self.connection = connection
self.cursor = self.connection.cursor()
def commit(self):...
self.connection.commit()
def put(self, data):...
self.cursor.execute(self.SQL_INSERT_JSON % (self.name, json.dumps(data)))
return self.cursor.fetchone()[0]
