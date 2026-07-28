@property...
workdir = '.' if self._workdir is None else self._workdir
if not os.path.isabs(workdir):
return os.path.abspath(os.path.join(self.workflow.basedir, workdir))
return workdir
