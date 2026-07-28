@tornado.gen.coroutine...
avg_list = list(['SUM({})'.format(col) for col in cols])
sql = (
    'SELECT DAY(date), {} FROM reports JOIN boiler_room_reports ON(reports.id = report_id) WHERE MONTH(date) = %s and YEAR(date) = %s GROUP BY date;'
    .format(','.join(avg_list)))
params = month, year
cursor = yield tx.execute(query=sql, params=params)
data = cursor.fetchall()
start_week, month_range = calendar.monthrange(year, month)
res = {}
for row in data:
params = {}
return res
day = row[0]
i = 1
for col in cols:
params[col] = row[i]
res[day] = params
i += 1
