def generate_sql(self, data, base_table):...
"""docstring"""
self.base_table = base_table
assert self.validate_where_data(data.get('where_data', {})
    ), 'Invalid where data'
where_phrase = self._generate_sql_condition(data['where_data'])
if 'group_by_fields' in data:
assert isinstance(data['group_by_fields'], list
    ), 'Group by fields need to list of dict'
path_subset = self.extract_paths_subset(list(map(lambda field_id: self.
    field_mapping[field_id][self.TABLE_NAME], data['fields'])), data.get(
    'path_hints', {}))
data['group_by_fields'] = list(map(lambda x: int(x['field']), data[
    'group_by_fields']))
join_tables = self.create_join_path(path_subset, self.base_table)
join_phrase = self.generate_left_join(join_tables)
group_by_phrase = self.generate_group_by(data.get('group_by_fields', []),
    data.get('having', {}))
count_phrase = u'COUNT(DISTINCT `{base_table}`.`id`)'.format(base_table=
    base_table)
return u'SELECT {count_phrase} FROM {base_table} {join_phrase} WHERE {where_phrase} {group_by_fragment}'.format(
    join_phrase=join_phrase, base_table=base_table, where_phrase=
    where_phrase, group_by_fragment=group_by_phrase, count_phrase=count_phrase)
