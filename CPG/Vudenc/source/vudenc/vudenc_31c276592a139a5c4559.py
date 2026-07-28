def create_join_path(self, path_map, curr_table):...
"""docstring"""
if curr_table not in path_map:
return
for table_name in sorted(path_map[curr_table]):
yield table_name, curr_table
for item in self.create_join_path(path_map, table_name):
yield item
