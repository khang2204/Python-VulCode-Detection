def resolve_dep(target, from_map, *args):...
errmsg = 'could not resolve dependency: %s' % target
ret = from_map[args]
if not ret:
return ret
