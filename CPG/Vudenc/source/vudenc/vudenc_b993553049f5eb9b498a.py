def validate_group_by_data(self, group_by_fields, having):...
"""docstring"""
assert isinstance(group_by_fields, list)
assert isinstance(having, dict)
for cond in self.extract_key_from_nested_dict(having, self.WHERE_CONDITION):
assert isinstance(cond, dict), 'where condition needs to be dict'
return True
assert 'aggregate_lhs' in cond or cond.get('field'
    ) in group_by_fields, 'Use of non aggregate value or non grouped field: {}'.format(
    cond)
