@tornado.gen.coroutine...
sql = 'SELECT {} FROM districts WHERE name = %s'.format(cols)
params = name,
cursor = yield tx.execute(query=sql, params=params)
return cursor.fetchone()
