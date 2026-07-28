def get_val(self, attr_name):...
"""docstring"""
value = None
if attr_name in vars(self):
value = getattr(self, attr_name)
return value
