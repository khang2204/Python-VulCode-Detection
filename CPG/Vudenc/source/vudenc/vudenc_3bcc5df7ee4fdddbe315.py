@tornado.gen.coroutine...
sql = 'SELECT {} FROM reports WHERE date = STR_TO_DATE(%s, %s)'.format(cols)
params = date, '%d.%m.%Y'
cursor = yield tx.execute(query=sql, params=params)
return cursor.fetchone()
