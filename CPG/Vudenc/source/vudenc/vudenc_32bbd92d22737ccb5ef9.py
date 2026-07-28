def get_requested_day_for_inverter(self, inverter_serial, date):...
data = dict()
day_start, day_end = self.get_epoch_day(date)
data['interval'] = {'from': self.convert_local_ts_to_utc(day_start, self.
    local_timezone), 'to': self.convert_local_ts_to_utc(day_end, self.
    local_timezone)}
query = """
            SELECT TimeStamp, Power 
            FROM DayData 
            WHERE TimeStamp BETWEEN %s AND %s AND Serial = %s;
            """
data['data'] = list()
for row in self.c.execute(query % (day_start, day_end, inverter_serial)):
data['data'].append({'time': row[0], 'power': row[1]})
if self.get_datetime(date).date() == datetime.today().date():
query = (
    """
                SELECT EToday
                FROM Inverters
                WHERE Serial = %s;
                """
     % inverter_serial)
query = (
    """
                SELECT DayYield AS Power 
                FROM MonthData 
                WHERE TimeStamp BETWEEN %s AND %s AND Serial = %s
                """
     % (day_start, day_end, inverter_serial))
self.c.execute(query)
res = self.c.fetchone()
if res and res[0]:
data['total'] = res[0]
data['total'] = 0
query = (
    """
            SELECT MIN(TimeStamp) as Min, MAX(TimeStamp) as Max 
            FROM ( SELECT TimeStamp FROM DayData WHERE Serial = %s );
            """
     % inverter_serial)
self.c.execute(query)
first_data, last_data = self.c.fetchone()
if first_data:
data['hasPrevious'] = first_data < day_start
data['hasPrevious'] = False
if last_data:
data['hasNext'] = last_data > day_end
data['hasNext'] = False
return data
