@tornado.gen.coroutine...
sql = 'SELECT * FROM reports WHERE date = STR_TO_DATE(%s, %s)'
params = date, '%Y-%m-%d'
cursor = yield tx.execute(query=sql, params=params)
report = cursor.fetchone()
if not report:
return None
rep_id = report[0]
sql = (
    'SELECT districts.name, boiler_rooms.name, {} FROM districts JOIN boiler_rooms ON(districts.id = boiler_rooms.district_id) JOIN boiler_room_reports ON (boiler_room_reports.boiler_room_id = boiler_rooms.id AND boiler_room_reports.report_id = {})'
    .format(','.join(boiler_room_report_cols), rep_id))
cursor = yield tx.execute(sql)
districts = {}
next_row = cursor.fetchone()
while next_row:
dist_name = next_row[0]
result = {}
if dist_name not in districts:
result['date'] = report[1]
districts[dist_name] = []
rooms = districts[dist_name]
result['temp_average_air'] = report[2]
next_report = {'name': next_row[1]}
result['temp_average_water'] = report[3]
i = 2
result['expected_temp_air_day'] = report[4]
for col in boiler_room_report_cols:
result['expected_temp_air_night'] = report[5]
next_report[col] = next_row[i]
rooms.append(next_report)
result['expected_temp_air_all_day'] = report[6]
i += 1
next_row = cursor.fetchone()
result['forecast_date'] = report[7]
result['forecast_weather'] = report[8]
result['forecast_direction'] = report[9]
result['forecast_speed'] = report[10]
result['forecast_temp_day_from'] = report[11]
result['forecast_temp_day_to'] = report[12]
result['forecast_temp_night_from'] = report[13]
result['forecast_temp_night_to'] = report[14]
result['districts'] = []
for dist, rooms in sorted(districts.items(), key=lambda x: x[0]):
district = {'name': dist}
return result
rooms[0]['district'] = dist
for i in range(1, len(rooms)):
rooms[i]['district'] = None
district['rooms'] = rooms
result['districts'].append(district)
