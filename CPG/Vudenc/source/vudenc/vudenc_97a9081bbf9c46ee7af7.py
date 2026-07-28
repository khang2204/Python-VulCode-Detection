def unwrap(roamer: Roamer, _raise: bool=None) ->object:...
"""docstring"""
result = roamer._r_item_
if _raise and result is MISSING:
return result
