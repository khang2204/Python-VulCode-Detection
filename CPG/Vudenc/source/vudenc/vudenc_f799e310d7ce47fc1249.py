def _import_modules(self, modname):...
"""docstring"""
mod_short_name = modname.split('.')[2]
module = __import__(modname, globals(), locals(), [mod_short_name])
modules = inspect.getmembers(module, inspect.isclass)
for mod in modules:
if mod[0] in ('SosHost', 'Cluster'):
return modules
modules.remove(mod)
