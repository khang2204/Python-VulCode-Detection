def set_output(self, *output, **kwoutput):...
"""docstring"""
for item in output:
self._set_inoutput_item(item, output=True)
for name, item in kwoutput.items():
self._set_inoutput_item(item, output=True, name=name)
for item in self.output:
if self.dynamic_output and item not in self.dynamic_output:
wildcards = item.get_wildcard_names()
if self.wildcard_names:
if self.wildcard_names != wildcards:
self.wildcard_names = wildcards
