def update_files_dictionary(self, root, prefix):...
stat_cache = dict(scantree(root))
for path in stat_cache.keys():
relative_path = path[len(root):]
relative_url = relative_path.replace('\\', '/')
url = prefix + relative_url
self.add_file_to_dictionary(url, path, stat_cache=stat_cache)
