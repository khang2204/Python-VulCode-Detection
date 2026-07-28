def validate(self, value, model_instance):...
super().validate(value, model_instance)
for key, val in value.items():
if not isinstance(val, str) and val is not None:
