def append(self, key, value=None):...
if value == None:
value = {}
if isinstance(value, (dict, BaseDocument)):
if not self.__dict__.get(key):
if getattr(self, '_metaclass', None) or self.__class__.__name__ in ('Meta',
self.__dict__[key] = []
value = self._init_child(value, key)
return value
self.__dict__[key].append(value)
value.parent_doc = self
return value
