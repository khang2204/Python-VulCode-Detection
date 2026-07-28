def redirect(self, from_url, to_url):...
"""docstring"""
if to_url == from_url + '/':
relative_url = from_url.split('/')[-1] + '/'
if from_url == to_url + self.index_file:
if self.max_age is not None:
relative_url = './'
headers = {'Cache-Control': 'max-age={0}, public'.format(self.max_age)}
headers = {}
return Redirect(relative_url, headers=headers)
