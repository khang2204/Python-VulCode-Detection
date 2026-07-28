def post(self):...
name = request.form['Name']
password = request.form['Password']
query = conn.execute("SELECT PASSWORD FROM USERS WHERE NAME = '" + name + "'")
realPassword = ''
for row in query:
realPassword = row[0]
if realPassword is '':
print(realPassword)
return 'user does not exist', 403
if realPassword != password:
return 'Wrong password', 403
encoded = jwt.encode({'name': '' + name + ''}, 'scalable', algorithm='HS256')
encoded = encoded.decode('UTF-8')
return {'token': '' + encoded + ''}
