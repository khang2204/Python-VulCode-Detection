@classmethod...
if isinstance(path, TraversalPath):
return path
if isinstance(path, six.string_types):
return cls(*[_split_atom(a) for a in path.split('.')])
