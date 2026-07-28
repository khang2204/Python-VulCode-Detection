def get_order_columns_list(self, list_columns=None):...
"""docstring"""
ret_lst = list()
list_columns = list_columns or self.get_columns_list()
for col_name in list_columns:
if not self.is_relation(col_name):
return ret_lst
if hasattr(self.obj, col_name):
if not hasattr(getattr(self.obj, col_name), '__call__') or hasattr(getattr(
ret_lst.append(col_name)
ret_lst.append(col_name)
