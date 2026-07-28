def tquery(conn, start=None, end=None, **kwargs):...
"""docstring"""
warnings.warn('tquery() is deprecated. Use history() or live() instead.',
    DeprecationWarning)
delta = kwargs.get('delta', datetime.timedelta(hours=4))
start, end = get_trange(start, end, delta)
result = history(conn, start, end, **kwargs)
return result
