def generate_left_join(self, join_path):...
join_phrases = []
for join_table, parent_table in join_path:
join_phrases.append(
    'LEFT JOIN {join_tbl} ON {join_tbl}.{join_fld} = {parent_tbl}.{parent_fld}'
    .format(join_tbl=join_table, parent_tbl=parent_table, join_fld=self.
    path_mapping[join_table][parent_table][self.JOIN_COLUMN], parent_fld=
    self.path_mapping[join_table][parent_table][self.PARENT_COLUMN]))
return ' '.join(join_phrases)
