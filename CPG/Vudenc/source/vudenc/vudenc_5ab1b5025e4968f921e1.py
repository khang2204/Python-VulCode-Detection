def install(self):...
logger = self.logger
src_path = self.src_path
dst_path = os.path.join(self.www_root, self.dst_path)
logger.info('Copying %s to %s' % (src_path, dst_path))
shutil.copytree(src_path, dst_path, symlinks=True)
logger.critical('Exception: {}'.format(e))
