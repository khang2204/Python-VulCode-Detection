def get_time(time):...
date_time = datetime.datetime
if time == 'NOW':
return date_time.now()
return date_time.strptime(time, '%Y%m%d %H%M%S')
