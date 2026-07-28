@memoized_property...
"""docstring"""
node_path = self.get_binary_path_from_tgz(supportdir=self._relpath, version
    =self.version, filename='node.tar.gz', inpackage_path='node')
logger.debug('Node path: %s', node_path)
return node_path
