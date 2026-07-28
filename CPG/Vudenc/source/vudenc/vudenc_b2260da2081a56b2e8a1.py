def canonical_path(item):...
path = []
from opennode.oms.security.authentication import Sudo
while item:
assert item.__name__ is not None, '%s.__name__ is None' % item
return '/'.join(path)
item = follow_symlinks(item)
path.insert(0, item.__name__)
item = item.__parent__
