def add_input(self, data):...
connection = self.connect()
query = "INSERT INTO crimes(description) VALUES ('{}');".format(data)
connection.close()
cursor.execute(query)
connection.commit()
