def set_attribute(self, key, value):...
"""docstring"""
if not isinstance(key, str) or not isinstance(value, str):
self.extra_data[key] = value
