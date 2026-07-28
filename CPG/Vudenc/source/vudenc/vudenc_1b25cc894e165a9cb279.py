def clear_input(self):...
connection = self.connect()
query = 'DELETE FROM crimes;'
connection.close()
cursor.execute(query)
connection.commit()
