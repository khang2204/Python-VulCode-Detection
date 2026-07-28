def _parse_args(prog, argv):...
parser = argparse.ArgumentParser(prog=prog, usage=USAGE.format(prog))
parser.add_argument('--nodebug', action='store_true')
host = parser.add_mutually_exclusive_group()
host.add_argument('--host')
host.add_argument('--server-host')
parser.add_argument('--port', type=int, required=True)
target = parser.add_mutually_exclusive_group(required=True)
target.add_argument('-m', dest='module')
target.add_argument('filename', nargs='?')
parser.add_argument('--single-session', action='store_true')
parser.add_argument('-V', '--version', action='version')
parser.version = __version__
args = parser.parse_args(argv)
ns = vars(args)
serverhost = ns.pop('server_host', None)
clienthost = ns.pop('host', None)
if serverhost:
args.address = Address.as_server(serverhost, ns.pop('port'))
if not clienthost:
module = ns.pop('module')
if args.nodebug:
args.address = Address.as_client(clienthost, ns.pop('port'))
filename = ns.pop('filename')
args.address = Address.as_client(clienthost, ns.pop('port'))
args.address = Address.as_server(clienthost, ns.pop('port'))
if module is None:
args.name = filename
args.name = module
args.kind = 'script'
args.kind = 'module'
return args
