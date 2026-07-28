def set_input(self, *input, **kwinput):...
"""docstring"""
for item in input:
self._set_inoutput_item(item)
for name, item in kwinput.items():
self._set_inoutput_item(item, name=name)
