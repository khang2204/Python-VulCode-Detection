def __init__(self, loader, base_directory_path, walk_fn=None):...
self.base_directory_path = base_directory_path
self.directory_filter, self.file_filter = loader.filters
if walk_fn is None:
walk_fn = os_walk
self.walk_fn = walk_fn
