def __init__(self, *args, **kwargs):...
args_len = len(args)
if args_len > len(self._meta.fields):
fields_iter = iter(self._meta.fields)
if args_len:
if not kwargs:
for field in fields_iter:
for val, field in zip(args, fields_iter):
for val, field in zip(args, fields_iter):
if kwargs:
val = kwargs.pop(field.attname)
val = field.get_default()
setattr(self, field.attname, val)
setattr(self, field.attname, val)
setattr(self, field.attname, val)
kwargs.pop(field.name, None)
