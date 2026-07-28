def add_file_to_dictionary(self, url, path, stat_cache=None):...
if self.is_compressed_variant(path, stat_cache=stat_cache):
return
if self.index_file and url.endswith('/' + self.index_file):
index_url = url[:-len(self.index_file)]
static_file = self.get_static_file(path, url, stat_cache=stat_cache)
index_no_slash = index_url.rstrip('/')
self.files[url] = static_file
self.files[url] = self.redirect(url, index_url)
self.files[index_no_slash] = self.redirect(index_no_slash, index_url)
url = index_url
