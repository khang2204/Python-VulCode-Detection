def get_entity(self):...
"""docstring"""
if self._accessor is None:
if self.__converted_entity is None:
self.__converted_entity = self.get_matching(self.get_id()).get_entity()
self.__converted_entity = self._convert_to_entity()
return self.__converted_entity
