def _sanity_check_path(self, src, dst, www_root):...
logger = self.logger
if not os.path.isdir(src):
msg = 'Source path: %s does not exist or is not a directory.' % src
if not os.path.isdir(www_root):
logger.critical(msg)
msg = 'Web root % s does not exist or is not a directory.' % src
www_root_abs = os.path.abspath(www_root)
logger.critical(msg)
rel_dst = dst
if os.path.isabs(dst):
_root = os.path.commonprefix([www_root_abs, dst])
_dst = os.path.join(www_root_abs, dst)
if _root is not www_root_abs:
_dst = os.path.realpath(_dst)
msg = ('Destination path is absolute and is not a subdirectory of web root. {}'
    .format([www_root, dst]))
rel_dst = os.path.relpath(www_root_abs, dst)
_root = os.path.commonprefix([www_root_abs, _dst])
logger.critical(msg)
abs_dst = os.path.join(www_root_abs, rel_dst)
if _root is not www_root_abs:
if os.path.exists(abs_dst):
msg = ('Destination is a relative path that resolves outside of web root. {}'
    .format([www_root_abs, dst]))
rel_dst = os.path.relpath(www_root_abs, _dst)
msg = 'Destination directory already exists: {}'.format(abs_dst)
return src, rel_dst, www_root_abs
logger.critical(msg)
logger.critical(msg)
