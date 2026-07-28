def generate_group_by(self, group_by_fields, having_clause):...
"""docstring"""
assert isinstance(group_by_fields, list)
assert isinstance(having_clause, dict)
assert self.validate_group_by_data(group_by_fields, having_clause
    ), 'Invalid having data'
if len(group_by_fields) == 0:
return ''
result = ''
fully_qualified_field_names = map(lambda field_id:
    '`{table_name}`.`{field_name}`'.format(table_name=self.field_mapping[
    field_id][self.TABLE_NAME], field_name=self.field_mapping[field_id][
    self.FIELD_NAME]), group_by_fields)
result += 'GROUP BY {fields}'.format(fields=', '.join(
    fully_qualified_field_names))
if len(having_clause.keys()) > 0:
result += ' HAVING {condition}'.format(condition=self.
    _generate_sql_condition(having_clause))
return result
