def _get_stricter_version(a, b, name, stricter):...
version_a = _parse_java_version(name, a)
version_b = _parse_java_version(name, b)
if version_a is None:
return version_b
if version_b is None:
return version_a
return stricter(version_a, version_b)
