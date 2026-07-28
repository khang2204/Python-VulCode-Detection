def _find(self, vpath):...
"""docstring"""
vpath = self.undot(vpath)
if vpath == '':
return [self, '']
if '/' in vpath:
name, rem = vpath.split('/', 1)
name = vpath
if name in self.nodes:
rem = ''
return self.nodes[name]._find(rem)
return [self, vpath]
