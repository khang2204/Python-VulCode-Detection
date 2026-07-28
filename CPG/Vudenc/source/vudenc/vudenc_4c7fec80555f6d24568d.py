"""
Entity cache and cache map.

This file is part of the everest project.
See LICENSE.txt for licensing, CONTRIBUTORS.txt for contributor information.

Created on Feb 26, 2013.
"""
from collections import defaultdict
from everest.repositories.memory.querying import MemoryQuery
from everest.repositories.state import EntityStateManager
from itertools import islice
from weakref import WeakValueDictionary
__docformat__ = 'reStructuredText en'
__all__ = ['EntityCache', 'EntityCacheMap']
"""
    Cache for entities.

    Supports add and remove operations as well as lookup by ID and
    by slug.
    """
def __init__(self, entities=None, allow_none_id=True):...
"""docstring"""
self.__allow_none_id = allow_none_id
if entities is None:
entities = []
self.__entities = entities
self.__id_map = WeakValueDictionary()
self.__slug_map = WeakValueDictionary()
def get_by_id(self, entity_id):...
"""docstring"""
return self.__id_map.get(entity_id)
