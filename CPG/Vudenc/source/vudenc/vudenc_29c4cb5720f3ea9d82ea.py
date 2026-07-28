def get_prep_value(self, value):...
value = super().get_prep_value(value)
if isinstance(value, dict):
prep_value = {}
if isinstance(value, list):
for key, val in value.items():
value = [str(item) for item in value]
return value
key = str(key)
value = prep_value
if val is not None:
val = str(val)
prep_value[key] = val
