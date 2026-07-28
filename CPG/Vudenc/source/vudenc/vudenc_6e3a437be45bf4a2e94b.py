def __init__(self, resource):...
if isinstance(resource, (list, tuple)):
self._resource_iters = [iter([(i, r) for i, r in enumerate(resource)])]
self._resource_iters = [iter([(None, resource)])]
self._field_iters = []
self._path = [(NotSupplied, NotSupplied, NotSupplied)]
self._resource_stack = [None]
