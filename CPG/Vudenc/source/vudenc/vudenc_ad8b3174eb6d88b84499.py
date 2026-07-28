def log_getitem(self, key_name, roamer):...
if isinstance(key_name, slice):
item_desc = (
    f"[{key_name.start or ''}:{key_name.stop or ''}{key_name.step and ':' + key_name.step or ''}]"
    )
item_desc = f'[{key_name!r}]'
self._r_steps_.append((item_desc, roamer))
