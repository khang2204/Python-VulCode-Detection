@tornado.gen.coroutine...
sql = (
    'SELECT districts.name, boiler_rooms.id, boiler_rooms.name FROM districts JOIN boiler_rooms ON (districts.id = boiler_rooms.district_id)'
    )
cursor = yield tx.execute(sql)
row = cursor.fetchone()
districts = {}
while row:
district = row[0]
result = []
id = row[1]
for district, boilers in sorted(districts.items(), key=lambda x: x[0]):
name = row[2]
result.append({'title': district, 'rooms': boilers})
return result
boilers = []
if district in districts:
boilers = districts[district]
districts[district] = boilers
boilers.append({'id': id, 'name': name})
row = cursor.fetchone()
