def _add_meta_props(self, response):...
"""docstring"""
for prop in sorted(self.r_handler.request.arguments):
prop_value = self.r_handler.get_query_argument(prop)
return response
if prop_value.isdigit():
prop_value = int(prop_value)
response[prop] = prop_value
