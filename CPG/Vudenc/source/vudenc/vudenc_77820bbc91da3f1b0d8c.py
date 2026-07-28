def clear_all(self):...
connection = self.connects()
query = 'DELETE FROM crimes;'
connection.close()
cursor.execute(query)
connection.commit()
