def __init__(self, wz_addr, fun, args=(), kvargs={}, name=None, start_timer...
super().__init__(*pargs, **pkvargs)
self.name = name if name else type(self).__name__
self.start_timer = start_timer
self.poll_timeout = poll_timeout if poll_timeout else 5 * 1000
self.call = fun, args, kvargs
self.wz_addr = wz_addr
self.wz_auth_requests = []
self.wz_bind_methods = []
self.wz_poll_timeout = 30
