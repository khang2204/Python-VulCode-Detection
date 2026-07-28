def registerUser(username, password, sqlHandle):...
conn = sqlHandle.connect()
cursor = conn.cursor()
userCheckQuery = "SELECT * FROM Users WHERE userEmail = '{0}'".format(username)
cursor.execute(userCheckQuery)
result = cursor.fetchone()
if result is not None:
return 'Fail'
queryString = ("INSERT INTO Users (userEmail, password) VALUES('{0}', '{1}');"
    .format(username, password))
cursor.execute(queryString)
conn.commit()
return 'Success'
