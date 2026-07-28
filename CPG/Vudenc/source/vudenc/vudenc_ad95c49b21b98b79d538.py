def get(self, key):...
if key in self.ime_property_cache:
return self.ime_property_cache[key]
return None
