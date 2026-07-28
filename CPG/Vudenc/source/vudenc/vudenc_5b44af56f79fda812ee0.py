def to_python(self, value):...
"""docstring"""
if value is None or value == '':
return {} if not self.null else None
while isinstance(value, str):
if isinstance(value, dict):
value = json_decode(value)
return JsonDict(**value)
if isinstance(value, str):
return JsonString(value)
if isinstance(value, list):
return JsonList(value)
return value
