def _parse_conditions(self, condition, data):...
"""docstring"""
sql = bytearray()
for element in data:
inner_condition = element.keys()[0]
return u'({})'.format(sql.decode('utf8'))
function = getattr(self, self.WHERE_CONDITION_MAPPING.get(inner_condition))
result = function(element.get(inner_condition))
if not sql and condition in [self.AND_CONDITION, self.OR_CONDITION]:
sql.extend('({})'.format(result))
sql.extend(' {0} ({1})'.format(condition, result))
