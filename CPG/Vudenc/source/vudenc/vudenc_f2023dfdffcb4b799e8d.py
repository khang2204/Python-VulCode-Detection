def get_user_columns_list(self):...
"""docstring"""
ret_lst = list()
for col_name in self.get_columns_list():
if not self.is_pk(col_name) and not self.is_fk(col_name):
return ret_lst
ret_lst.append(col_name)
