def with_timeout(f):...
@functools.wraps(f)...
timeout = kwargs.pop('timeout', None)
gt = eventlet.spawn(f, self, *args, **kwargs)
if timeout is None:
return gt.wait()
kill_thread = eventlet.spawn_after(timeout, gt.kill)
res = gt.wait()
kill_thread.cancel()
return __inner
return res
