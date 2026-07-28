def clear_all(self):...
connection = self.connect()
query = 'DELETE FROM crimes;'
connection.close()
cursor.execute(query)
connection.commit()
