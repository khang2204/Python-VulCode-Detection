@tornado.gen.coroutine...
sql = (
    'SELECT boiler_room_id, DAY(date), {} FROM boiler_room_reports JOIN reports ON(report_id = reports.id) WHERE YEAR(date) = %s AND MONTH(date) = %s'
    .format(','.join(columns)))
params = year, month
cursor = yield tx.execute(query=sql, params=params)
boilers = {}
row = cursor.fetchone()
while row:
boiler_id = row[0]
return boilers
day = row[1]
parameters = {}
if boiler_id in boilers:
parameters = boilers[boiler_id]
boilers[boiler_id] = parameters
for i in range(2, len(columns) + 2):
val = row[i]
row = cursor.fetchone()
col = columns[i - 2]
values = {}
if col in parameters:
values = parameters[col]
parameters[col] = values
values[day] = val
