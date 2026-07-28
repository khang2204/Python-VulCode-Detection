def __hash__(self):...
"""docstring"""
data_id = self.get_id()
return data_id is None and id(self._data) or hash((self._get_entity_type(),
    data_id))
