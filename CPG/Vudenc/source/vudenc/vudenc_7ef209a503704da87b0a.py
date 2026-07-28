def get_url_with_query_params(self, new_query_dict):...
query = dict(self.query_params).copy()
for key, value in query.items():
if type(value) == list:
query.update(new_query_dict)
query[key] = value[0]
for key, value in query.copy().items():
if value is None:
return '?{}'.format(urlencode(query))
