def __init__(self, param, menu_cls, remember=True, **kw):...
self.nav = menu_cls
self.remember = remember
param = menu_cls.get_param, param
Validator.__init__(self, param, **kw)
