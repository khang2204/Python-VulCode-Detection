def get(self, key=None, filters=None, limit=None, default=None):...
if key:
if isinstance(key, dict):
return self.__dict__
return _filter(self.get_all_children(), key, limit=limit)
if filters:
if isinstance(filters, dict):
value = self.__dict__.get(key, default)
value = _filter(self.__dict__.get(key, []), filters, limit=limit)
default = filters
if value is None and key not in self.ignore_in_getter and key in (d.
filters = None
self.set(key, [])
return value
value = self.__dict__.get(key, default)
value = self.__dict__.get(key)
