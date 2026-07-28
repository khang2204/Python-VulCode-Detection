def __init__(self, entities=None, allow_none_id=True):...
"""docstring"""
self.__allow_none_id = allow_none_id
if entities is None:
entities = []
self.__entities = entities
self.__id_map = WeakValueDictionary()
self.__slug_map = WeakValueDictionary()
