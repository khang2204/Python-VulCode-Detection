def validate(self):...
"""docstring"""
if self._validated_binaries:
return
if self._minimum_version:
version = self._get_version(java)
if self._maximum_version:
if version < self._minimum_version:
version = self._get_version(java)
self._bin_path = os.path.join(self.home, 'bin')
if version > self._maximum_version:
self._validated_executable('javac')
if self._jdk:
self._is_jdk = True
logger.debug(
    'Failed to validate javac executable. Please check you have a JDK installed. Original error: {}'
    .format(e))
