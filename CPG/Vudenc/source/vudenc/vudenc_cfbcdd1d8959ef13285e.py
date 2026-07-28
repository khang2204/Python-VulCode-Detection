from . import pathexpr
from . import ds
from . import fs
def __init__(self, compileddoc, startingpath):...
self._doc = compileddoc
self._root = startingpath
def get_rule_names(self):...
return self._doc['rules'].keys()
