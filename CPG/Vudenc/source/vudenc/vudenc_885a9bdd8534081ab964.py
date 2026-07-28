def get_search_columns_list(self):...
ret_lst = list()
for col_name in self.get_columns_list():
if not self.is_relation(col_name):
return ret_lst
tmp_prop = self.get_property_first_col(col_name).name
ret_lst.append(col_name)
if not self.is_pk(tmp_prop) and not self.is_fk(tmp_prop) and not self.is_image(
ret_lst.append(col_name)
