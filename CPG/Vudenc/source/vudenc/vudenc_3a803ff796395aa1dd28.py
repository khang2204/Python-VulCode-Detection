def __init__(self, *args, **kwargs):...
default = kwargs.get('default', None)
if default is not None:
kwargs['default'] = pickle.dumps(default)
super().__init__(*args, **kwargs)
