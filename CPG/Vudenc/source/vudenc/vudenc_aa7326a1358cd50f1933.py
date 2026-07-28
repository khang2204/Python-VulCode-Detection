def get_tag(self, tagname):...
"""docstring"""
values = []
for entry in self.entries:
if entry.tag_name == tagname:
return values
values.append(entry.value)
