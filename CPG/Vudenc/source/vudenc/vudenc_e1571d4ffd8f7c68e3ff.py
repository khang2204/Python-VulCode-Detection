def format(self, value):...
if isinstance(value, datetime.datetime) or isinstance(value, datetime.date):
return localize(value)
return value
