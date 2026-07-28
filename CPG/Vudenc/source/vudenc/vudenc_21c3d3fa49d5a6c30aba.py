def store_to_file(self, request):...
if self.log_dir is None:
return
filename = '%s_%s.log' % (request.start_time, request.__class__.__name__)
filepath = os.path.join(self.log_dir, filename)
linkpath = os.path.join(self.log_dir, request.__class__.__name__)
request.store_to_file(fd)
os.remove(linkpath)
os.symlink(filename, linkpath)
