def _get_explicit_jdk_paths(self):...
if not self._normalized_jdk_paths:
return ()
os_name = normalize_os_name(os.uname()[0].lower())
if os_name not in self._normalized_jdk_paths:
logger.warning(
    '--jvm-distributions-paths was specified, but has no entry for "{}".'.
    format(os_name))
return self._normalized_jdk_paths.get(os_name, ())
