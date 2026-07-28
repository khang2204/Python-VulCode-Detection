def strip_hash(h, keys):...
if not keys:
return h
for k in keys.split('.'):
if k in h and isinstance(h[k], dict):
return h
h = h[k]
