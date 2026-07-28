@tornado.gen.coroutine...
sql = (
    'SELECT month(date) as month, day(date) as day FROM reports WHERE year(date) = %s'
    )
params = year,
cursor = yield tx.execute(query=sql, params=params)
return cursor.fetchall()
