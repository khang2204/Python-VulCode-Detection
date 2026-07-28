def protected(value):...
"""docstring"""
if is_flagged(value, 'temp'):
return flag(value, 'protected')
