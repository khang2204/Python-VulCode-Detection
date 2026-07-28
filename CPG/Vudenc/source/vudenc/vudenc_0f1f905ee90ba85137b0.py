def _set_params_item(self, item, name=None):...
if isinstance(item, str) or callable(item):
self.params.append(item)
start = len(self.params)
if name:
for i in item:
self.params.add_name(name)
self._set_params_item(i)
if name:
self.params.set_name(name, start, end=len(self.params))
