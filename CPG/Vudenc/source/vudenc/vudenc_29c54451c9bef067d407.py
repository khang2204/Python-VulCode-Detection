def retrieve_file(self, path):...
"""docstring"""
destdir = self.config['tmp_dir'] + '/'
dest = destdir + path.split('/')[-1]
if not self.local:
self.log_debug('Failed to retrieve %s: %s' % (path, err))
if self.file_exists(path):
self.log_debug('Moving %s to %s' % (path, destdir))
return False
self.log_debug('Copying remote %s to local %s' % (path, destdir))
self.log_debug(
    'Attempting to copy remote file %s, but it does not exist on filesystem' %
    path)
shutil.copy(path, dest)
self.sftp.get(path, dest)
return False
return True
