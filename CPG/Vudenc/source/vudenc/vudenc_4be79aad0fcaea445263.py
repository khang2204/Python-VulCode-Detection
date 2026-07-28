def default(self, obj):...
if isinstance(obj, Promise):
return force_unicode(obj)
return super(LazyEncoder, self).default(obj)
