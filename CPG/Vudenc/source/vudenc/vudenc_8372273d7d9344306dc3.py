def traverse1(path):...
"""docstring"""
from opennode.oms.zodb import db
oms_root = db.get_root()['oms_root']
objs, untraversed_path = traverse_path(oms_root, path)
if objs and not untraversed_path:
return objs[-1]
return None
