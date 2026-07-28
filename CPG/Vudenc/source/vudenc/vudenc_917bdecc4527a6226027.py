@contextlib.contextmanager...
if timeout is None:
timeout = self.TIMEOUT
lock, wait = get_locked_and_waiter()
def handler(msg):...
if not match(msg):
return msg, False
lock.release()
return msg, True
