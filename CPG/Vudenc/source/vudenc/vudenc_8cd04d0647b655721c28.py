def __init__(self, src_path, dst_path, www_root, logger=None):...
self.logger = logger or logging.getLogger('ContentInstaller')
_src, _dst, _www = self._sanity_check_path(src_path, dst_path, www_root)
self.src_path = _src
self.dst_path = _dst
self.www_root = _www
