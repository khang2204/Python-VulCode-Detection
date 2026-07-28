def live(conn, delta=None, **kwargs):...
"""docstring"""
if delta is None:
delta = {'hours': 4}
if isinstance(delta, datetime.timedelta):
if isinstance(delta, dict):
end = datetime.datetime.now()
delta = datetime.timedelta(**delta)
start = end - delta
return history(conn, start, end, **kwargs)
