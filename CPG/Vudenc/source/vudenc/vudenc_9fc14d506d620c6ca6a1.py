def is_periodic(self, value):...
"""docstring"""
m = self.regex.search(value)
if m is not None:
return m.group('value')
