import calendar
from datetime import date as libdate
import tornado
import tornado.gen
boiler_room_report_cols = ['T1', 'T2', 'gas_pressure', 'boilers_all',
    'boilers_in_use', 'torchs_in_use', 'boilers_reserve',
    'boilers_in_repair', 'net_pumps_in_work', 'net_pumps_reserve',
    'net_pumps_in_repair', 'all_day_expected_temp1',
    'all_day_expected_temp2', 'all_day_real_temp1', 'all_day_real_temp2',
    'all_night_expected_temp1', 'all_night_expected_temp2',
    'all_night_real_temp1', 'all_night_real_temp2', 'net_pressure1',
    'net_pressure2', 'net_water_consum_expected_ph',
    'net_water_consum_real_ph', 'make_up_water_consum_expected_ph',
    'make_up_water_consum_real_ph', 'make_up_water_consum_real_pd',
    'make_up_water_consum_real_pm', 'hardness', 'transparency']
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
