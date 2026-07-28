def init_valid_columns(self):...
for key in default_fields:
if key not in self.__dict__:
for key in self.get_valid_columns():
self.__dict__[key] = None
if key in ('idx', 'docstatus') and self.__dict__[key] is None:
if key not in self.__dict__:
self.__dict__[key] = 0
self.__dict__[key] = None
