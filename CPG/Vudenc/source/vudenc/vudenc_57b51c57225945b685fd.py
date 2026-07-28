def _generate_sql_condition(self, data):...
"""docstring"""
result = ''
if data:
condition = data.keys()[0]
return result
function = getattr(self, self.WHERE_CONDITION_MAPPING.get(condition))
result = function(data[condition])
