def file_exists(self, fname):...
"""docstring"""
if not self.local:
self.sftp.stat(fname)
return False
os.stat(fname)
return False
return True
return True
