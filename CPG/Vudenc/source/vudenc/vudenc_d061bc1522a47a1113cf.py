def parse_args(argv=None):...
"""docstring"""
if argv is None:
argv = sys.argv
prog = argv[0]
prog = argv[0]
argv = argv[1:]
if prog == __file__:
supported, pydevd, script = _group_args(argv)
prog = '{} -m ptvsd'.format(os.path.basename(sys.executable))
args = _parse_args(prog, supported)
extra = pydevd + ['--']
if script:
extra += script
return args, extra
