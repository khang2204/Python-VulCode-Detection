def close(self, fd):...
"""docstring"""
if not fd:
return True
if self.tempfiles[fd] is not None:
shasum = hashlib.sha256(open(self.tempfiles[fd], 'rb').read()).hexdigest()
return os.close(fd)
shasumfile = self.cfg.get('honeypot', 'download_path') + '/' + shasum
if os.path.exists(shasumfile):
os.remove(self.tempfiles[fd])
os.rename(self.tempfiles[fd], shasumfile)
self.update_realfile(self.getfile(self.filenames[fd]), shasumfile)
log.msg(format='SFTP Uploaded file "%(filename)s" to %(outfile)s', eventid=
    'cowrie.session.file_upload', filename=os.path.basename(self.filenames[
    fd]), outfile=shasumfile, shasum=shasum)
