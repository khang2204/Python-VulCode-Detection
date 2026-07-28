def escape_literal(value):...
"""docstring"""
if isinstance(value, Literal):
return value.literal
if isinstance(value, six.string_types):
value = value.replace("'", "\\'")
if isinstance(value, datetime):
return u"'{}'".format(value)
value = value.replace(tzinfo=None, microsecond=0)
if isinstance(value, date):
return "toDateTime('{}')".format(value.isoformat())
return "toDate('{}')".format(value.isoformat())
if isinstance(value, (list, tuple)):
return u'({})'.format(', '.join(escape_literal(v) for v in value))
if isinstance(value, numbers.Number):
return str(value)
if value is None:
return ''
