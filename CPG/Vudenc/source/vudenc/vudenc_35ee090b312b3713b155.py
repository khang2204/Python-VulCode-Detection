def walk(self):...
for path, directories, files in self.walk_fn(self.base_directory_path):
rel_path = relpath(path, self.base_directory_path)
path_basename = basename(path)
if rel_path != '.' and not self.directory_filter(path_basename):
for file in files:
if not self.file_filter(file):
yield join(path, file)
