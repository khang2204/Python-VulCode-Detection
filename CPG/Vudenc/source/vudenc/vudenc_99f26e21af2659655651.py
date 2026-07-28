def __getattr__(self, attr_name):...
if self._r_item_ is MISSING:
if not self._r_via_alternate_lookup_:
copy = Roamer(self)
self._r_path_.log_getattr(attr_name, self)
return self
if self._r_is_multi_item_:
multi_items = []
copy._r_item_ = getattr(copy._r_item_, attr_name)
copy._r_item_ = MISSING
if copy._r_item_ is MISSING and not self._r_via_alternate_lookup_:
for i in self._r_item_:
if not self._r_via_alternate_lookup_:
self._r_via_alternate_lookup_ = True
copy._r_path_.log_getattr(attr_name, copy)
if copy._r_item_ is MISSING and copy._r_raise_:
lookup = None
copy._r_item_ = tuple(multi_items)
copy._r_path_.log_getattr(attr_name, copy)
copy = self[attr_name]
self._r_via_alternate_lookup_ = False
return copy
lookup = getattr(i, attr_name)
if isinstance(lookup, (tuple, list, range)):
lookup = i[attr_name]
multi_items += lookup
if lookup is not None:
multi_items.append(lookup)
