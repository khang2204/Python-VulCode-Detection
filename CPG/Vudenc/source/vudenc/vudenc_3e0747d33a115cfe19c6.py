def render(obj):...
if isinstance(obj, set):
return list(obj)
if hasattr(obj, '__str__'):
return str(obj)
log.msg('RENDERING ERROR, cannot json serialize %s' % obj, system='httprest')
