@tornado.gen.coroutine...
sql = (
    'SELECT date, {} FROM reports JOIN boiler_room_reports ON(reports.id = report_id) WHERE YEAR(date) = %s AND boiler_room_id = %s'
    .format(','.join(columns)))
params = year, id
cursor = yield tx.execute(query=sql, params=params)
data = cursor.fetchall()
res = {}
for row in data:
params = {}
return res
date = row[0]
day = date.timetuple().tm_yday
i = 1
for col in columns:
params[col] = row[i]
res[day] = params
i += 1
