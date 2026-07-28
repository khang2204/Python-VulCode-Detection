def get_data(type):...
from datetime import datetime
from pytz import timezone
import sql
now_utc = datetime.now(timezone(sql.get_setting('time_zone')))
if type == 'config':
fmt = '%Y-%m-%d.%H:%M:%S'
if type == 'logs':
fmt = '%Y%m%d'
if type == 'date_in_log':
fmt = '%b %d %H:%M:%S'
return now_utc.strftime(fmt)
