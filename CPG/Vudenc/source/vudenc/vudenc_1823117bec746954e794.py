def __init__(self, rate_user=False, rate_ip=False, prefix='rate_', *a, **kw):...
self.rate_user = rate_user
self.rate_ip = rate_ip
self.prefix = prefix
Validator.__init__(self, *a, **kw)
