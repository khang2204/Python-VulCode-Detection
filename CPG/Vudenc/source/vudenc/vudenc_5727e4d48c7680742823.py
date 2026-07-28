def get_form_fields(self):...
ret = []
for field in self.FORM:
if field in self.meta.iptc_keys:
return ret
ret.append((field, self.get_safe_value(self.meta, field)))
ret.append((field, ''))
