def _parse_custom_method_condition(self, data):...
"""docstring"""
assert isinstance(data, dict), 'Input data must be a dict'
assert 'template_id' in data, 'No template_id is provided'
template_id = int(data['template_id'])
template_data = self.custom_methods[template_id]
validated_parameters = {}
for param_id, param_data in data.get('parameters', {}).items():
assert param_id in template_data[self.TEMPLATE_PARAMS_KEY
    ], 'Invalid parameter name.'
template_params = template_data[self.TEMPLATE_PARAMS_KEY].keys()
param_type = template_data[self.TEMPLATE_PARAMS_KEY][param_id]['data_type']
assert len(set(template_params) ^ set(validated_parameters.keys())
    ) == 0, 'Missing or extra template variable'
validated_parameters[param_id] = self._process_parameter(param_type, param_data
    )
return template_data[self.TEMPLATE_STR_KEY].format(**validated_parameters)
