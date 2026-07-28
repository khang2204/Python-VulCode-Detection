def __init__(self, binary_util, relpath, version, package_manager,...
self._binary_util = binary_util
self._relpath = relpath
self._version = self._normalize_version(version)
self.package_manager = self.validate_package_manager(package_manager=
    package_manager)
self.yarnpkg_version = self._normalize_version(version=yarnpkg_version)
logger.debug('Node.js version: %s package manager from config: %s', self.
    _version, package_manager)
