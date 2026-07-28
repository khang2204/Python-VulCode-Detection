def description(self):...
result = []
first_missing_index, first_missing_desc, _ = self._first_missing()
if first_missing_index:
result.append(
    f'missing step {first_missing_index} {first_missing_desc} for path ')
result.append(f'<{type(self._r_root_item_).__name__}>')
result += [desc for desc, _ in self._r_steps_]
if first_missing_index:
_, _, last_found_roamer = self._last_found()
return ''.join(result)
if last_found_roamer:
result.append(f' at <{type(last_found_roamer()).__name__}>')
last_found_data = last_found_roamer()
if isinstance(last_found_data, (tuple, list, set, range)):
if re.match('\\[\\d+\\]', first_missing_desc):
if isinstance(last_found_data, (str, int, float, complex, bool, bytes,
result.append(f' with length {len(last_found_data)}')
keys = last_found_data.keys()
attrs = dir(last_found_data)
if keys:
if attrs and not isinstance(last_found_data, (str, tuple, list)):
result.append(f" with keys [{', '.join([repr(k) for k in keys])}]")
result.append(
    f" with attrs [{', '.join([a for a in attrs if not a.startswith('_')])}]")
