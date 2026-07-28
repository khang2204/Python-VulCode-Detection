def _ConvertToAscii(value):...
"""docstring"""
if isinstance(value, str):
return value
if isinstance(value, unicode):
return value.encode('utf-8')
return str(value)
