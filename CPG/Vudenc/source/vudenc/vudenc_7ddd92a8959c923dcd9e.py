def chown(self, item, owner):...
"""docstring"""
if type(item) == str:
item = self.locate(item)
def _chown_recursive(item_, owner_):...
if not item:
for sub_ in item_.sub_items:
return False
_chown_recursive(sub_, owner_)
item_.owner = owner_
if item_.is_dir:
self._update_in_db(item_)
return
