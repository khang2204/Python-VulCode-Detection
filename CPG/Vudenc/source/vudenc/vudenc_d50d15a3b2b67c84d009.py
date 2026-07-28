@memoized_property...
normalized = {}
jdk_paths = self.get_options().paths or {}
for name, paths in sorted(jdk_paths.items()):
rename = normalize_os_name(name)
return normalized
if rename in normalized:
logger.warning('Multiple OS names alias to "{}"; combining results.'.format
    (rename))
normalized[rename] = paths
normalized[rename].extend(paths)
