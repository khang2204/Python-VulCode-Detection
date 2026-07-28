@tornado.gen.coroutine...
sql = 'INSERT INTO users(email, pass_hash) VALUES (%s, %s)'
params = email, pass_hash
yield tx.execute(query=sql, params=params)
