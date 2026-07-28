@tornado.gen.coroutine...
sql = (
    'SELECT boiler_rooms.id, boiler_rooms.name, districts.name from boiler_rooms JOIN districts ON(districts.id = district_id)'
    )
cursor = yield tx.execute(query=sql)
tuples = cursor.fetchall()
res = []
for t in tuples:
res.append({'id': t[0], 'title': '%s - %s' % (t[2], t[1])})
return res
