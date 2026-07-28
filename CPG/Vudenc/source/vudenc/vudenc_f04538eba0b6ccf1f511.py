def __call__(self, *args, _raise=False, _roam=False, _invoke=None, **kwargs):...
if _raise and self._r_item_ is MISSING:
if _invoke is not None:
call_result = _invoke(self._r_item_, *args, **kwargs)
if callable(self._r_item_):
if _roam:
call_result = self._r_item_(*args, **kwargs)
if args or kwargs:
copy = Roamer(self)
return call_result
call_result = self._r_item_(*args, **kwargs)
call_result = self._r_item_
copy._r_item_ = call_result
return copy
