def __init__(self, initial_item, path_to_clone=None):...
if path_to_clone is not None:
self._r_root_item_ = path_to_clone._r_root_item_
self._r_root_item_ = initial_item
self._r_steps_ = list(path_to_clone._r_steps_)
self._r_steps_ = []
