def _sanitize_value(self, value, data_type):...
"""docstring"""
if data_type == self.INTEGER:
if data_type == self.DATE:
int(value)
if data_type == self.DATE_TIME:
datetime.datetime.strptime(value, '%Y-%m-%d')
datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
