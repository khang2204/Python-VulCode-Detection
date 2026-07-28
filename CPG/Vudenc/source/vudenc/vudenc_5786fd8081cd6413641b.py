def __init__(self, request):...
self.request = request
for traversal_name, object_name, factory in (('activities', 'activity',
self[traversal_name] = TraversalDbAccess(self, traversal_name, object_name,
    factory)
self['configfiles'] = TraversalDbAccess(self, 'configfiles', 'config_file',
    ConfigFiles, 'key')
