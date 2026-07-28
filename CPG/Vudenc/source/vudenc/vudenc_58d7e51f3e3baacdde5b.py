def postpone(function):...
"""docstring"""
def decorator(*args, **ka):...
t = Thread(target=function, args=args, kwargs=ka)
t.daemon = True
t.start()
return decorator
