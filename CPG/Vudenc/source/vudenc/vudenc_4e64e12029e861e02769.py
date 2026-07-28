def add_cache_headers(self, headers, path, url):...
if self.immutable_file_test(path, url):
headers['Cache-Control'] = 'max-age={0}, public, immutable'.format(self.FOREVER
    )
if self.max_age is not None:
headers['Cache-Control'] = 'max-age={0}, public'.format(self.max_age)
