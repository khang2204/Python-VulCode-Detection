def get_safe_value(self, meta, key):...
"""docstring"""
val = meta[key].value
logger.warn('%s could not get meta for %s', self, key)
if meta[key].repeatable:
return ''
return val
return val[0]
