def __init__(self, parent, traversal_name, object_name, factory, id_key='id'):...
self.__parent__ = parent
self.factory = factory
self.object_name = object_name
self.__name__ = traversal_name
self.id_key = id_key
