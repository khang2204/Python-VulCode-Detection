def validate(self, value, model_instance):...
super().validate(value, model_instance)
for index, part in enumerate(value):
if isinstance(self.base_field, ArrayField):
self.base_field.validate(part, model_instance)
if len({len(i) for i in value}) > 1:
