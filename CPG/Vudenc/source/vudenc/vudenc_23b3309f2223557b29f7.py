def _convert_values(self, values, data_type):...
"""docstring"""
if data_type in [self.CHOICE, self.MULTICHOICE]:
if data_type in self.CONVERSION_REQUIRED:
int(values[0])
wrapper = "'{value}'"
wrapper = '{value}'
wrapper = "'{value}'"
wrapper = '{value}'
return (wrapper.format(value=value) for value in values)
