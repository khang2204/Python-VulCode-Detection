def get_static_file(self, path, url, stat_cache=None):...
if stat_cache is None and not os.path.exists(path):
headers = Headers([])
self.add_mime_headers(headers, path, url)
self.add_cache_headers(headers, path, url)
if self.allow_all_origins:
headers['Access-Control-Allow-Origin'] = '*'
if self.add_headers_function:
self.add_headers_function(headers, path, url)
return StaticFile(path, headers.items(), stat_cache=stat_cache, encodings={
    'gzip': path + '.gz', 'br': path + '.br'})
