def update_if_missing(self, d):...
if isinstance(d, BaseDocument):
d = d.get_valid_dict()
if 'doctype' in d:
self.set('doctype', d.get('doctype'))
for key, value in iteritems(d):
if self.get(key
self.set(key, value)
