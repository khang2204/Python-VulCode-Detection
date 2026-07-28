def get_pk_name(self):...
for col_name in self.list_columns.keys():
if self.is_pk(col_name):
return col_name
