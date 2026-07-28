def lseek(self, fd, offset, whence):...
"""docstring"""
if not fd:
return True
return os.lseek(fd, offset, whence)
