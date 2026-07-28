def _parse_multi_path_mapping(self, paths):...
"""docstring"""
path_map = defaultdict(dict)
for join_tbl, join_fld, parent_tbl, parent_fld in paths:
assert parent_tbl not in path_map[join_tbl
    ], 'Joins with multiple fields is not supported'
return path_map
path_map[join_tbl][parent_tbl] = {self.PARENT_COLUMN: parent_fld, self.
    JOIN_COLUMN: join_fld}
