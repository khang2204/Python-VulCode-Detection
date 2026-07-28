def _to_int(s, default, mi=None, mx=None):...
if not s.isdigit():
return default
_n = int(s)
if mi != None and _n < mi:
return default
if mx != None and _n > mx:
return default
return _n
