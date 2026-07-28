def __init__(self, toclone=None, fromdict=None, plainstr=False):...
"""docstring"""
list.__init__(self)
self._names = dict()
if toclone:
self.extend(map(str, toclone) if plainstr else toclone)
if fromdict:
if isinstance(toclone, Namedlist):
for key, item in fromdict.items():
self.take_names(toclone.get_names())
self.append(item)
self.add_name(key)
