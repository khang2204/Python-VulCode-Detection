def get_int_columns(self):...
result = {}
for col_name, col in self.columns.items():
if col.type is 'int':
return result
result[col_name] = col.get_display_name()
