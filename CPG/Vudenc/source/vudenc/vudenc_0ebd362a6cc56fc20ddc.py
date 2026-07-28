def get_value(self, fieldname):...
df = self.meta.get_field(fieldname)
val = self.get(fieldname)
return self.cast(val, df)
