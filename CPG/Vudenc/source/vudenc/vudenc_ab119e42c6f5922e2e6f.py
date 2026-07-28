def open(self, filename, openFlags, mode):...
"""docstring"""
if openFlags & os.O_WRONLY == os.O_WRONLY or openFlags & os.O_RDWR == os.O_RDWR:
hostmode = mode & ~111
if openFlags & os.O_RDONLY == os.O_RDONLY:
hostfile = '%s/%s_sftp_%s' % (self.cfg.get('honeypot', 'download_path'),
    time.strftime('%Y%m%d-%H%M%S'), re.sub('[^A-Za-z0-9]', '_', filename))
return None
return None
self.mkfile(filename, 0, 0, 0, stat.S_IFREG | mode)
fd = os.open(hostfile, openFlags, hostmode)
self.update_realfile(self.getfile(filename), hostfile)
self.tempfiles[fd] = hostfile
self.filenames[fd] = filename
return fd
