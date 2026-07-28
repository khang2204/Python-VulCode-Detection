def _parse_java_version(name, version):...
if isinstance(version, string_types):
version = Revision.lenient(version)
if version and not isinstance(version, Revision):
return version
