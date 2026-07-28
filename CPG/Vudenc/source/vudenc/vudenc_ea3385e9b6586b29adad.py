def get_trange(start, end, delta):...
"""docstring"""
if not isinstance(start, datetime.datetime) or not isinstance(end, datetime
if not isinstance(delta, datetime.timedelta):
if end < start:
if not isinstance(start, datetime.datetime):
return start, end
if not isinstance(end, datetime.datetime):
if not isinstance(end, datetime.datetime):
end = datetime.datetime.now()
start = end - delta
end = start + delta
