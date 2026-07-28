def update(self, d):...
if 'doctype' in d:
self.set('doctype', d.get('doctype'))
for key in default_fields:
if key in d:
for key, value in iteritems(d):
self.set(key, d.get(key))
self.set(key, value)
return self
