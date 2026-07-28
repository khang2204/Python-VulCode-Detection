def _include_filters(obj):...
for key in filters.__all__:
if not hasattr(obj, key):
setattr(obj, key, getattr(filters, key))
