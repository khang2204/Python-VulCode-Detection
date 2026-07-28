def add_to_class(cls, name, value):...
if hasattr(value, 'contribute_to_class'):
value.contribute_to_class(cls, name)
setattr(cls, name, value)
