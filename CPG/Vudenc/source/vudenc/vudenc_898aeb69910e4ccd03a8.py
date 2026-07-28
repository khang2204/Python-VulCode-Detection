def set(self, key, value, as_value=False):...
if isinstance(value, list) and not as_value:
self.__dict__[key] = []
self.__dict__[key] = value
self.extend(key, value)
