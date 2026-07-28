def get_related_fk(self, model):...
for col_name in self.list_properties.keys():
if self.is_relation(col_name):
if model == self.get_related_model(col_name):
return col_name
