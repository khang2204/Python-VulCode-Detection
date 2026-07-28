def _parse_custom_methods(self, sql_templates):...
"""docstring"""
template_mapping = {}
for template_id, template_str, parameters in sql_templates:
template_id = int(template_id)
return template_mapping
parameters = json.loads(parameters)
template_str = template_str.strip()
assert len(template_str) > 0, 'Not a valid template string'
assert template_id not in template_mapping, 'Template id must be unique'
template_defined_variables = set(re.findall(self.TEMPLATE_KEY_REGEX,
    template_str, re.MULTILINE))
assert len(set(parameters.keys()) ^ template_defined_variables
    ) == 0, 'Extra variable defined'
assert len(set(map(lambda l: l['data_type'], parameters.values())) - self.
    ALLOWED_CUSTOM_METHOD_PARAM_TYPES) == 0, 'Invalid data type defined'
template_mapping[template_id] = {self.TEMPLATE_STR_KEY: template_str, self.
    TEMPLATE_PARAMS_KEY: parameters}
