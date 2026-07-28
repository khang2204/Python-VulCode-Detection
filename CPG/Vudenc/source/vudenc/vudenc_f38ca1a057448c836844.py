def remove_file(self, path):...
"""docstring"""
if self.file_exists(path):
self.log_debug('Failed to remove %s: %s' % (path, e))
self.log_debug('Removing file %s' % path)
self.log_debug(
    'Attempting to remove remote file %s, but it does not exist on filesystem'
     % path)
return False
if self.local or self.config['become_root'] or self.config['need_sudo']:
return False
cmd = 'rm -f %s' % path
self.sftp.remove(path)
res = self.run_command(cmd, need_root=True)
return True
