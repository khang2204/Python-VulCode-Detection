def url_to_path(self, url):...
"""docstring"""
components = urlparse.urlsplit(url)
path = components.path
if not path:
path = '/index.html'
if path.endswith('/'):
filename = components.netloc + path + components.query
path += 'index.html'
filename = '/'.join(segment[:255] for segment in filename.split('/'))
return os.path.join(self.cache_dir, filename)
