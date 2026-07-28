def __init__(self, name=None, directory=None, options=None, conf={},...
self.conf = conf
self.parents = set()
self.children = set()
self.name = name
self.directory = directory
self.options = options or {}
self.exclude_from_cmake = exclude_from_cmake
self.external_project = external_project
self.toplevel = toplevel
