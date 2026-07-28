def __str__(self):...
if self.fatal:
if not len(self.deps):
return self.message + ' Install packages: %s' % ' '.join(self.deps)
return self.message + ' Unresolvable.'
return self.message + ' Unresolvable.  Partially resolvable with packages: %s' % ' '.join(
    self.deps)
