def post(self):...
print(request.json)
Name = request.json['Name']
Password = request.json['Password']
query = conn.execute("INSERT INTO USERS(NAME, PASSWORD) VALUES ('" + Name +
    "', '" + Password + "')")
conn.commit()
return {'status': 'success'}
