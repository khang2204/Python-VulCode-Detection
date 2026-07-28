def is_nullable(self, col_name):...
if self.is_relation_many_to_one(col_name):
col = self.get_relation_fk(col_name)
return self.list_columns[col_name].nullable
return False
return col.nullable
