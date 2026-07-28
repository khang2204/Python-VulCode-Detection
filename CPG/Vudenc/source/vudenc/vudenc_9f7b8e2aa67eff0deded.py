def find_file(self, url):...
if not self.index_file and url.endswith('/'):
return
if not self.url_is_canonical(url):
return
for path in self.candidate_paths_for_url(url):
return self.find_file_at_path(path, url)
