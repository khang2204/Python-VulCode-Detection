def __init__(self, item, _raise=None):...
if isinstance(item, Roamer):
for attr in ('_r_item_', '_r_is_multi_item_', '_r_raise_'):
self._r_item_ = item
setattr(self, attr, getattr(item, attr))
self._r_path_ = _Path(item._r_item_, item._r_path_)
self._r_path_ = _Path(self._r_item_)
if _raise is not None:
self._r_raise_ = bool(_raise)
