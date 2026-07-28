def clean(self, value) ->dict:...
value = super().clean(value)
if self.one_required and (not value or not any(v for v in value)):
if self.require_all_fields and not all(v for v in value):
return value
