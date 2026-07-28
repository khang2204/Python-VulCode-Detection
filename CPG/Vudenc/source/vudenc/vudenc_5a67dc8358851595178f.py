def _process_parameter(self, data_type, parameter_data):...
assert len(data_type) > 0, 'Invalid data type'
assert isinstance(parameter_data, dict), 'Invalid parameter data format'
if data_type.upper() == 'FIELD':
field_data = self.field_mapping[parameter_data['field']]
if data_type.upper() == 'INTEGER':
return '`{table}`.`{field}`'.format(table=field_data[self.TABLE_NAME],
    field=field_data[self.FIELD_NAME])
return int(parameter_data['value'])
if data_type.upper() == 'STRING':
return parameter_data['value']
