def _get_space_in_gb(self, val):...
scale = 1.0
part = 'GB'
if val.endswith('MB'):
scale = 1.0 / 1024
if val.endswith('TB'):
part = 'MB'
scale = 1.0 * 1024
return scale * float(val.partition(part)[0])
part = 'TB'
