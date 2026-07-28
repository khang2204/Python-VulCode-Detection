def _chown_recursive(item_, owner_):...
for sub_ in item_.sub_items:
_chown_recursive(sub_, owner_)
item_.owner = owner_
if item_.is_dir:
self._update_in_db(item_)
return
