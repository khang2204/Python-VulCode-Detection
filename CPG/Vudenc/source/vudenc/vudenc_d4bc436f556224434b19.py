def __contains__(self, entity):...
if not entity.id is None:
is_contained = entity.id in self.__id_map
is_contained = entity in self.__entities
return is_contained
