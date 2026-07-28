@tornado.gen.coroutine...
sql = 'DELETE FROM reports WHERE date = %s'
params = date,
cursor = yield tx.execute(query=sql, params=params)
return cursor.fetchone()
