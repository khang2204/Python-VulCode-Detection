def get_columns(self):...
result = {}
for col_name, col in self.columns.items():
result[col_name] = col.get_display_name()
return result
