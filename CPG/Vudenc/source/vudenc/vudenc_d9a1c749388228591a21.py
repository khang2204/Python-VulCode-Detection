def get_content(self, item):...
"""docstring"""
if type(item) == str:
item = self.locate(item)
if not item:
return b''
if item.is_dir:
return b''
return FileStorage.get_content(item.f_uuid)
