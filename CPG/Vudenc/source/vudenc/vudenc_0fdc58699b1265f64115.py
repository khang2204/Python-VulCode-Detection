def __init__(self, fd, newfd):...
self.fd = fd
self.backup = os.dup(fd)
filename, mode = newfd
self.newfd = newfd
self.newfd = os.open(filename, mode)
