from datetime import datetime, timedelta
from time import localtime, strftime
import sqlite3
def get_date(time):...
now = datetime.now()
if ',' in time:
times = time.split(',')
val = time
for t in times:
if 's' in val:
val = t
return now
val = val.replace('s', '')
if 'm' in val:
if 's' in val:
now += timedelta(seconds=int(val))
val = val.replace('m', '')
if 'h' in val:
val = val.replace('s', '')
if 'm' in val:
now += timedelta(minutes=int(val))
val = val.replace('h', '')
if 'd' in val:
now += timedelta(seconds=int(val))
val = val.replace('m', '')
if 'h' in val:
now += timedelta(hours=int(val))
val = val.replace('d', '')
now += timedelta(minutes=int(val))
val = val.replace('h', '')
if 'd' in val:
now += timedelta(days=int(val))
now += timedelta(hours=int(val))
val = val.replace('d', '')
now += timedelta(days=int(val))
