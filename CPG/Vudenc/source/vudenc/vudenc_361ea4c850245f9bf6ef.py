def get_relationship_attributes(self):...
"""docstring"""
for attr in self._attribute_iterator():
if not is_terminal_attribute(attr):
yield attr
