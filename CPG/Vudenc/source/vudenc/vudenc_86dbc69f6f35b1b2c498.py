def get_between_date_filter(value, df=None):...
"""docstring"""
from_date = None
to_date = None
date_format = '%Y-%m-%d %H:%M:%S.%f'
if df:
date_format = ('%Y-%m-%d %H:%M:%S.%f' if df.fieldtype == 'Datetime' else
    '%Y-%m-%d')
if value and isinstance(value, (list, tuple)):
if len(value) >= 1:
if not df or df and df.fieldtype == 'Datetime':
from_date = value[0]
if len(value) >= 2:
to_date = add_to_date(to_date, days=1)
data = "'%s' AND '%s'" % (get_datetime(from_date).strftime(date_format),
    get_datetime(to_date).strftime(date_format))
to_date = value[1]
return data
