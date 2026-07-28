def subworkflow(self, name, snakefile=None, workdir=None):...
sw = Subworkflow(self, name, snakefile, workdir)
self._subworkflows[name] = sw
self.globals[name] = sw.target
