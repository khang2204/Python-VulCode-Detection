@tornado.gen.coroutine...
sql = 'SELECT date, temp_average_air FROM reports WHERE YEAR(date) = %s'
params = year,
cursor = yield tx.execute(query=sql, params=params)
data = cursor.fetchall()
res = {}
for row in data:
day = row[0].timetuple().tm_yday
return res
res[day] = row[1]
