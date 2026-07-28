def target(self, paths):...
if not_iterable(paths):
return flag(os.path.join(self.workdir, paths), 'subworkflow', self)
return [self.target(path) for path in paths]
