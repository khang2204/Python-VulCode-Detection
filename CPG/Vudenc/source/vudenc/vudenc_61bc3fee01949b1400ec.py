def scrub_ch_data(data, meta):...
data = [{c[0]: d[i] for i, c in enumerate(meta)} for d in data]
meta = [{'name': m[0], 'type': m[1]} for m in meta]
for col in meta:
if DATETIME_TYPE_RE.match(col['type']):
return data, meta
for d in data:
if DATE_TYPE_RE.match(col['type']):
d[col['name']] = d[col['name']].replace(tzinfo=tz.tzutc()).isoformat()
for d in data:
dt = datetime(*d[col['name']].timetuple()[:6]).replace(tzinfo=tz.tzutc())
d[col['name']] = dt.isoformat()
