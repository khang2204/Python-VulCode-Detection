def default(obj):...
import datetime
if isinstance(obj, datetime.datetime):
return datetime.datetime.strftime(obj, '%Y-%m-%d %H:%M:%S')
