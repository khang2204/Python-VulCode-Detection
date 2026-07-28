def get(self):...
query = conn.execute('SELECT * FROM USERS')
i = 0
for row in query:
i = i + 1
return {'Number of users': i}
