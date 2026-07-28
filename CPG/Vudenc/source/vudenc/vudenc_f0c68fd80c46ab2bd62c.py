def __eq__(self, other):...
if isinstance(other, Roamer):
return other._r_item_ == self._r_item_
return other == self._r_item_
