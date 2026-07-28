def get_all_inputs(self):...
connection = self.connects()
query = 'SELECT description FROM crimes;'
connection.close()
cursor.execute(query)
return cursor.fetchall()
