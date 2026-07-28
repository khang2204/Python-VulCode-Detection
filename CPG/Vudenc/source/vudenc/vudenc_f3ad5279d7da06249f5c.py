def _walk(directory_filter, file_filter):...
def __init__(self, filters):...
self.filters = filters
loader = MockLoader(filters=[directory_filter, file_filter])
walk_fn = create_mock_os_walk(MOCK_START_PATH)
walker = FileWalker(loader, MOCK_START_PATH, walk_fn=walk_fn)
return [f for f in walker.walk()]
