def compress(self, data_list) ->dict:...
data = {}
data['_scheme'] = self.scheme_name
for i, value in enumerate(data_list):
data[self.scheme['fields'][i][0]] = value or ''
return data
