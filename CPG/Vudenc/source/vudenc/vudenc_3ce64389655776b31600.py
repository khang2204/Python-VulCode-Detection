def to_python(self, value):...
if isinstance(value, str):
vals = json.loads(value)
return value
value = [self.base_field.to_python(val) for val in vals]
