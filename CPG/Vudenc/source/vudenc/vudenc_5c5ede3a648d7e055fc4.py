def find_file_at_path(self, path, url):...
if self.is_compressed_variant(path):
if self.index_file:
return self.find_file_at_path_with_indexes(path, url)
return self.get_static_file(path, url)
