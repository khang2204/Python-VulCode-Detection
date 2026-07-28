def do_request(self, url, data=None, file_names=None):...
"""docstring"""
if file_names is None:
if data is None:
data = data.copy()
for fobj in file_objs.itervalues():
return response
response = self.session.get(url)
data = data.copy()
data['_xsrf'] = self.xsrf_token
fobj.close()
data['_xsrf'] = self.xsrf_token
file_objs = dict((k, io.open(v, 'rb')) for k, v in file_names)
response = self.session.post(url, data)
response = self.session.post(url, data, files=file_objs)
