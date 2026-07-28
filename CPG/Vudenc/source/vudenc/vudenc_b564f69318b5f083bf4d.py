def set_params(self, *params, **kwparams):...
for item in params:
self._set_params_item(item)
for name, item in kwparams.items():
self._set_params_item(item, name=name)
