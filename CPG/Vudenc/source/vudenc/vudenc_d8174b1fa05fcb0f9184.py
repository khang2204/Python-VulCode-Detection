def __init__(self, d):...
self.update(d)
self.dont_update_if_missing = []
if hasattr(self, '__setup__'):
self.__setup__()
