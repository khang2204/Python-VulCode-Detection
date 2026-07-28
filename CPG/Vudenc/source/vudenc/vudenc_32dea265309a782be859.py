def remove(self, entity):...
"""docstring"""
self.__id_map.pop(entity.id, None)
self.__slug_map.pop(entity.slug, None)
self.__entities.remove(entity)
