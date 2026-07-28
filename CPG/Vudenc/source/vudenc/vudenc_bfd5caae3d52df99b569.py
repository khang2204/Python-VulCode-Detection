def __next__(self):...
if self._r_item__iter is None:
next_value = next(self._r_item__iter)
return Roamer(next_value)
