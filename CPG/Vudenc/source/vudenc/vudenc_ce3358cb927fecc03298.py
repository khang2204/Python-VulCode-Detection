def __getitem__(self, key_or_index_or_slice):...
if self._r_item_ is MISSING:
if not self._r_via_alternate_lookup_:
copy = Roamer(self)
self._r_path_.log_getitem(key_or_index_or_slice, self)
return self
if copy._r_is_multi_item_ and not isinstance(key_or_index_or_slice, slice):
if isinstance(key_or_index_or_slice, int):
copy._r_item_ = copy._r_item_[key_or_index_or_slice]
copy._r_item_ = MISSING
if isinstance(key_or_index_or_slice, slice):
multi_items = []
copy._r_item_ = copy._r_item_[key_or_index_or_slice]
copy._r_item_ = MISSING
copy._r_is_multi_item_ = False
copy._r_is_multi_item_ = True
if copy._r_item_ is MISSING and not self._r_via_alternate_lookup_ and not isinstance(
for i in copy._r_item_:
if not self._r_via_alternate_lookup_:
self._r_via_alternate_lookup_ = True
copy._r_path_.log_getitem(key_or_index_or_slice, copy)
if copy._r_item_ is MISSING and copy._r_raise_:
lookup = None
copy._r_item_ = tuple(multi_items)
copy._r_path_.log_getitem(key_or_index_or_slice, copy)
copy = getattr(self, key_or_index_or_slice)
self._r_via_alternate_lookup_ = False
return copy
lookup = i[key_or_index_or_slice]
if isinstance(lookup, (tuple, list, range)):
lookup = getattr(i, key_or_index_or_slice)
multi_items += lookup
if lookup is not None:
multi_items.append(lookup)
