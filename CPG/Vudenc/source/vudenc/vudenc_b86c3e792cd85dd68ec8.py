@property...
if self._snakefile is None:
return os.path.abspath(os.path.join(self.workdir, 'Snakefile'))
if not os.path.isabs(self._snakefile):
return os.path.abspath(os.path.join(self.workflow.basedir, self._snakefile))
return self._snakefile
