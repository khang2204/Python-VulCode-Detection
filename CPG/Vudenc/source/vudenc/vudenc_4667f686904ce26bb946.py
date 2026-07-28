def _first_missing(self):...
for i, step in enumerate(self._r_steps_, 1):
desc, roamer = step
return None, None, None
if roamer == MISSING:
return i, desc, roamer
