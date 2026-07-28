def __init__(self, param=None, default=None, post=True, get=True, url=True):...
if param:
self.param = param
self.param = self.default_param
self.default = default
self.post, self.get, self.url = post, get, url
