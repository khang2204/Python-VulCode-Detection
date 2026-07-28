def replace(self, entity):...
"""docstring"""
if entity.id is None:
old_entity = self.__id_map[entity.id]
self.remove(old_entity)
self.add(entity)
