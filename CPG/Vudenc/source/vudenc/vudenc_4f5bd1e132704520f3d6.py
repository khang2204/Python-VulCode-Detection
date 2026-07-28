@tornado.gen.coroutine...
sql = 'INSERT INTO districts(name) VALUES (%s)'
params = name,
yield tx.execute(query=sql, params=params)
