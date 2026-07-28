def tuplify(nested):...
if isinstance(nested, (list, tuple)):
return tuple(tuplify(child) for child in nested)
return nested
