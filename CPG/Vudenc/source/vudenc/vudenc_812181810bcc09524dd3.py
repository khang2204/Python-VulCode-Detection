def workdir(self, workdir):...
if self.overwrite_workdir is None:
if not os.path.exists(workdir):
os.makedirs(workdir)
self._workdir = workdir
os.chdir(workdir)
