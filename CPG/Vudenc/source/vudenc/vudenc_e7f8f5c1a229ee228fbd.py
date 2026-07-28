def get_title(self):...
if isinstance(self.model_field, SmartListFilter):
return self.model_field.title
return super(SmartFilter, self).get_title()
