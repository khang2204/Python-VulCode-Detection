def __init__(self, base_field, size=None, **kwargs):...
self.base_field = base_field
self.size = size
if self.size:
self.default_validators = [*self.default_validators,
    ArrayMaxLengthValidator(self.size)]
if hasattr(self.base_field, 'from_db_value'):
self.from_db_value = self._from_db_value
super().__init__(**kwargs)
