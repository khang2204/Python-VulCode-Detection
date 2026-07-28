def __init__(self, verbose_name=None, name=None, encoder=None, **kwargs):...
if encoder and not callable(encoder):
self.encoder = encoder
super().__init__(verbose_name, name, **kwargs)
