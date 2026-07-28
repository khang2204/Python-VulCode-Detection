def get_all_inputs(self):...
connection = self.connect()
query = 'SELECT description FROM crimes'
connection.close()
cursor.execute(query)
return cursor.fetchall()
