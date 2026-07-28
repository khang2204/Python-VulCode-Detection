def get_prep_value(self, value):...
if value is not None:
return JsonAdapter(value, encoder=self.encoder)
return value
