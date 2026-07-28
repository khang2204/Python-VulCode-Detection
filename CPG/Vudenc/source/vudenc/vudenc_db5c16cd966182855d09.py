def run(self, key, name):...
if key:
uid = cache.get(str(self.cache_prefix + '_' + key))
c.errors.add(errors.EXPIRED)
a = Account._byID(uid, data=True)
return None
if name and a.name.lower() != name.lower():
c.errors.add(errors.BAD_USERNAME)
if a:
return a
