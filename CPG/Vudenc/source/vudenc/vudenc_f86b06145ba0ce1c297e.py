def _scan_constraint_match(self, minimum_version, maximum_version, jdk):...
"""docstring"""
for dist in self._cache.values():
if minimum_version and dist.version < minimum_version:
if maximum_version and dist.version > maximum_version:
if jdk and not dist.jdk:
return dist
