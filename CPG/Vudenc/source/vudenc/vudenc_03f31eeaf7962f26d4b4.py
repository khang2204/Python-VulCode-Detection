@memoized_property...
"""docstring"""
yarnpkg_path = self.get_binary_path_from_tgz(supportdir='bin/yarnpkg',
    version=self.yarnpkg_version, filename='yarnpkg.tar.gz', inpackage_path
    ='dist')
logger.debug('Yarnpkg path: %s', yarnpkg_path)
return yarnpkg_path
