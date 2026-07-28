def validate_where_data(self, where_data):...
"""docstring"""
assert isinstance(where_data, dict) and len(where_data
    ) > 0, 'Invalid or empty where data'
for cond in self.extract_key_from_nested_dict(where_data, self.WHERE_CONDITION
assert isinstance(cond, dict), 'Invalid where condition'
return True
assert cond.get('aggregate_lhs', ''
    ) == '', 'Use of non aggregate value or non grouped field: {}'.format(cond)
