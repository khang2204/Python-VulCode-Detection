def _last_found(self):...
last_found_step = None, None, None
for i, step in enumerate(self._r_steps_, 1):
desc, roamer = step
return last_found_step
if roamer != MISSING:
last_found_step = i, desc, roamer
