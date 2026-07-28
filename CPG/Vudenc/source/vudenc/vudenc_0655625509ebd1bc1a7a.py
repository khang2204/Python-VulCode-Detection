def __init__(self, data, accessor, relationship_direction):...
"""docstring"""
super(DataTraversalProxy, self).__init__()
self.relationship_direction = relationship_direction
self._data = data
self._accessor = accessor
self._relationships = {}
