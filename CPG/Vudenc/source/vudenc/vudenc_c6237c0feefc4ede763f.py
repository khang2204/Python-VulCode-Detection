def find_file_at_path_with_indexes(self, path, url):...
if url.endswith('/'):
path = os.path.join(path, self.index_file)
if url.endswith('/' + self.index_file):
return self.get_static_file(path, url)
if os.path.isfile(path):
return self.get_static_file(path, url)
if os.path.isfile(os.path.join(path, self.index_file)):
return self.redirect(url, url[:-len(self.index_file)])
return self.redirect(url, url + '/')
