def to_route(self):...
"""docstring"""
clone = self.clone()
if clone.charset is None:
slash = b'/'
slash = '/'
route = slash + slash.join(clone.parts)
if clone._trailing_slash:
route += slash
return route
