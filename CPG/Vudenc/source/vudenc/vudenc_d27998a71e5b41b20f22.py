def contains(self, prefix):...
"""docstring"""
if prefix == '/':
return True
path = self.to_route()
return len(path) >= len(prefix) and path.startswith(prefix) and (len(path) ==
    len(prefix) or path[len(prefix)] == '/')
