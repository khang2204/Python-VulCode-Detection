def add_mime_headers(self, headers, path, url):...
media_type = self.media_types.get_type(path)
if media_type.startswith('text/') or media_type == 'application/javascript':
params = {'charset': str(self.charset)}
params = {}
headers.add_header('Content-Type', str(media_type), **params)
