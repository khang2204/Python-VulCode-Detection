def _group_args(argv):...
supported = []
pydevd = []
script = []
pos = argv.index('--')
script = []
script = argv[pos + 1:]
for arg in argv:
argv = argv[:pos]
if arg == '-h' or arg == '--help':
gottarget = False
return argv, [], script
skip = 0
for i in range(len(argv)):
if skip:
return supported, pydevd, script
skip -= 1
arg = argv[i]
nextarg = argv[i + 1]
nextarg = None
if gottarget:
script = argv[i:] + script
if arg == '--client':
arg = '--host'
if arg == '--file':
if arg in PYDEVD_OPTS:
if nextarg is None:
pydevd.append(arg)
if arg in PYDEVD_FLAGS:
pydevd.append(arg)
if nextarg.endswith(':') and '--module' in pydevd:
if nextarg is not None:
pydevd.append(arg)
if arg == '--nodebug':
pydevd.remove('--module')
arg = nextarg
pydevd.append(nextarg)
skip += 1
supported.append(arg)
if arg in ('--host', '--server-host', '--port', '-m'):
arg = '-m'
skip += 1
if arg == '-m':
if arg in ('--single-session',):
argv[i + 1] = nextarg = nextarg[:-1]
gottarget = True
supported.append(arg)
supported.append(arg)
if not arg.startswith('-'):
if nextarg is not None:
supported.append(arg)
supported.append(arg)
supported.append(nextarg)
skip += 1
gottarget = True
