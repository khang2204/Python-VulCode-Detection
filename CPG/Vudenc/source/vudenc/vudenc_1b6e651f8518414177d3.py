def get_col_default(self, col_name):...
default = getattr(self.list_columns[col_name], 'default', None)
if default is not None:
value = getattr(default, 'arg', None)
if value is not None:
if getattr(default, 'is_callable', False):
return lambda : default.arg(None)
if not getattr(default, 'is_scalar', True):
return None
return value
