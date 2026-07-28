def merge_cfg(dest, source):...
for k, v in source.items():
if isinstance(v, dict):
return dest
subdest = dest.setdefault(k, {})
dest[k] = v
merge_cfg(subdest, v)
