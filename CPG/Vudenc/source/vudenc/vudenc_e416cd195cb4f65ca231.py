def add(self, entity):...
"""docstring"""
if not entity.id is None:
if entity.id in self.__id_map:
if not self.__allow_none_id:
self.__id_map[entity.id] = entity
if hasattr(entity, 'slug') and not entity.slug is None:
if entity.slug in self.__slug_map:
self.__entities.append(entity)
self.__slug_map[entity.slug] = entity
