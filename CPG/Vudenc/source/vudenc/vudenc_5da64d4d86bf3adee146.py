def __init__(self, *args, **kwargs):...
null = kwargs.get('null', False)
default = kwargs.get('default', None)
self.encoder = kwargs.get('encoder', None)
if not null and default is None:
kwargs['default'] = '{}'
if isinstance(default, (list, dict)):
kwargs['default'] = json_encode(default, cls=self.encoder, sort_keys=True)
models.Field.__init__(self, *args, **kwargs)
