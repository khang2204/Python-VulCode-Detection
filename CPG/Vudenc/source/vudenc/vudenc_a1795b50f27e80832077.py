def pass_limit(bound):...
if isinstance(bound, list):
ds, ls = zip(*bound)
return points >= bound
for i, d in enumerate(ds):
if pad_points:
return True
p = d_points.get(d, 0)
if d_points.get(d, 0) < ls[i]:
l = ls[i]
return False
if p < l:
for j in range(i + 1, len(ds)):
jd = ds[j]
jp = d_points.get(jd, 0)
if jp > l - p:
d_points[jd] -= l - p
p += jp
d_points[d] = l
d_points[d] = p
d_points[jd] = 0
