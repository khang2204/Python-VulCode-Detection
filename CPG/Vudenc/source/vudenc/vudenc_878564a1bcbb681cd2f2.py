def monotonic_time():...
"""docstring"""
now = time.time()
if now > _last_now:
_last_now = now
return _last_now
