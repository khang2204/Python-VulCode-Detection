@tornado.gen.coroutine...
sql = ('SELECT {} FROM boiler_rooms WHERE district_id = %s AND name = %s'.
    format(cols))
params = dist_id, name
cursor = yield tx.execute(query=sql, params=params)
return cursor.fetchone()
