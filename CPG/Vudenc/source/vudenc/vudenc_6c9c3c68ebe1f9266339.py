def parse_known_args(self, args=None, namespace=None, nohelp=False):...
"""docstring"""
if nohelp:
args = sys.argv[1:] if args is None else args
return super().parse_known_args(args, namespace)
args = [a for a in args if a != '-h' and a != '--help']
