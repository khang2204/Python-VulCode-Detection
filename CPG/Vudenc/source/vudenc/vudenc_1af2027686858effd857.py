def to_python(self, value):...
if not value:
return None
_value = value
if isinstance(_value, str):
_value = bytes(_value, encoding='utf-8')
return pickle.loads(_value)
return super().to_python(value)
_value = base64.b64decode(_value)
