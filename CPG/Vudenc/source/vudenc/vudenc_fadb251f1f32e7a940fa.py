def _generate_where_phrase(self, where):...
"""docstring"""
if not isinstance(where, dict):
operator, value, field, secondary_value = self._get_validated_data(where)
field_name = self.field_mapping[field][self.FIELD_NAME]
sql_operator = getattr(self.VALUE_OPERATORS, operator)
data_type = self._get_data_type(field)
table = self._get_table_name(field)
if sql_operator == self.VALUE_OPERATORS.is_op:
assert value.upper() in self.IS_OPERATOR_VALUE, 'Invalid rhs for `IS` operator'
self._sanitize_value(value, data_type)
sql_value, secondary_sql_value = value.upper(), None
if secondary_value:
lhs = u'`{table}`.`{field}`'.format(table=table, field=field_name)
self._sanitize_value(secondary_value, data_type)
if data_type == self.STRING:
if 'aggregate_lhs' in where:
value = self._sql_injection_proof(value)
sql_value, secondary_sql_value = self._convert_values([value,
    secondary_value], data_type)
aggregate_func_name = where['aggregate_lhs'].upper()
if sql_operator in [self.VALUE_OPERATORS.is_challenge_completed, self.
if secondary_value:
if aggregate_func_name in self.ALLOWED_AGGREGATE_FUNCTIONS:
return '{negate} {check}'.format(negate='NOT' if sql_operator == self.
    VALUE_OPERATORS.is_challenge_not_completed else '', check=self.
    CHALLENGE_CHECK_QUERY.format(value=sql_value))
if sql_operator == self.BETWEEN:
secondary_value = self._sql_injection_proof(secondary_value)
lhs = u'{func_name}({field_name})'.format(func_name=aggregate_func_name,
    field_name=lhs)
logger.info('Unsupported aggregate functions: {}'.format(aggregate_func_name))
where_phrase = (u'{lhs} {operator} {primary_value} AND {secondary_value}'.
    format(lhs=lhs, operator=sql_operator, value=sql_value, secondary_value
    =secondary_sql_value))
where_phrase = u'{lhs} {operator} {value}'.format(operator=sql_operator,
    lhs=lhs, value=sql_value)
return where_phrase
