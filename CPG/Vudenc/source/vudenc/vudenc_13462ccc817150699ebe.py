@property...
"""docstring"""
for attr in self._attribute_iterator():
if attr.kind != RESOURCE_ATTRIBUTE_KINDS.COLLECTION:
attr_val = self._get_proxied_attribute_value(attr)
yield attr, attr_val
