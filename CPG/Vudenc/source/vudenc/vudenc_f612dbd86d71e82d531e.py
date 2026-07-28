def __init__(self, *args, path_separator=DEFAULT_PATH_SEPARATOR,...
self._sep = path_separator
self._data = {}
self._create_on_missing = create_on_missing(path_factory)
self.update(*args, **kwargs)
