def to_abs_str(self):...
"""docstring"""
path = self.to_str()
if not path.startswith('/'):
path = '/' + path
return path
