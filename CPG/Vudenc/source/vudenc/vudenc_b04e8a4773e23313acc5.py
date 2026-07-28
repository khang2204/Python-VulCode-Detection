def run_validators(self, value):...
super().run_validators(value)
for index, part in enumerate(value):
self.base_field.run_validators(part)
