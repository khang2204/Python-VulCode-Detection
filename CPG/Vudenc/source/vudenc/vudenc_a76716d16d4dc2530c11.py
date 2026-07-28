@tornado.gen.coroutine...
sql = 'SELECT {} FROM users WHERE email = %s'.format(cols)
params = email
cursor = yield tx.execute(query=sql, params=params)
return cursor.fetchone()
