@tornado.gen.coroutine...
sql = 'INSERT INTO boiler_rooms(district_id, name) VALUES (%s, %s)'
params = dist_id, name
yield tx.execute(query=sql, params=params)
