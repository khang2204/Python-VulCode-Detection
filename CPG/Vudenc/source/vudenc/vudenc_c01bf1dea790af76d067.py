def _find_modules_in_path(self, path, modulename):...
"""docstring"""
modules = []
if os.path.exists(path):
for pyfile in sorted(os.listdir(path)):
return modules
if not pyfile.endswith('.py'):
if '__' in pyfile:
fname, ext = os.path.splitext(pyfile)
modname = 'soscollector.%s.%s' % (modulename, fname)
modules.extend(self._import_modules(modname))
