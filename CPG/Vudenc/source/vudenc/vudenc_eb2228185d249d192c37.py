def __init__(self, param, min=None, max=None, error=errors.BAD_NUMBER, *a, **kw...
self.min = min
self.max = max
self.error = error
Validator.__init__(self, param, *a, **kw)
