def thread_safe_client(client, lock=None):...
"""docstring"""
if lock is None:
lock = threading.Lock()
return _ThreadSafeProxy(client, lock)
