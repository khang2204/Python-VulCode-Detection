def resolve_methods(self, parts):...
if parts:
method = parts[0]
yield 'index', parts
vpath = parts[1:]
yield method, vpath
