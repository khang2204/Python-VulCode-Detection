def clean_fields(self, exclude=None):...
errors = {}
for f in self._meta.fields:
if exclude and f.name in exclude:
if errors:
raw_value = f.value_from_object(self)
if f.null and raw_value is None:
raw_value = f.clean(raw_value)
errors[f.name] = e.messages
clean_method = getattr(self, 'clean_%s' % f.attname, None)
if callable(clean_method):
setattr(self, f.attname, raw_value)
raw_value = clean_method(raw_value)
errors.setdefault(f.name, []).extend(e.messages)
