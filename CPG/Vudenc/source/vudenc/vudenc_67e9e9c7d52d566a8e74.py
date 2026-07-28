def get_binary_path_from_tgz(self, supportdir, version, filename,...
tarball_filepath = self._binary_util.select_binary(supportdir=supportdir,
    version=version, name=filename)
logger.debug('Tarball for %s(%s): %s', supportdir, version, tarball_filepath)
work_dir = os.path.dirname(tarball_filepath)
unpacked_dir = os.path.join(work_dir, 'unpacked')
if not os.path.exists(unpacked_dir):
TGZ.extract(tarball_filepath, tmp_dist)
binary_path = os.path.join(unpacked_dir, inpackage_path)
os.rename(tmp_dist, unpacked_dir)
return binary_path
