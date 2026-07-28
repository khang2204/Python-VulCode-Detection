def dump_options(module):...
for key, value in sorted(module.options.items()):
if value is None:
cmakelists_rows.append('unset(%s CACHE)\n' % key)
if isinstance(value, bool):
kind = 'BOOL'
kind = 'STRING'
value = 'ON' if value else 'OFF'
cmakelists_rows.append('set(%s %s CACHE INTERNAL "" FORCE)\n' % (key, value))
