def select(self, target):...
if not isinstance(target, JvmTarget):
return False
return target.has_sources('.java') or target.has_sources('.scala')
