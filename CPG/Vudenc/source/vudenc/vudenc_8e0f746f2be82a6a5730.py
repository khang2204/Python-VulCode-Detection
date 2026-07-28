def date_format(date_time):...
"""docstring"""
if date_time is None:
return ''
return date_time.strftime(DATE_FORMAT)
