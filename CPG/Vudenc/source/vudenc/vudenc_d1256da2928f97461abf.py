def _call(self, msg, args, errorSink=None):...
userargs = [args.name]
kindstr = ''
if args.kind is not None:
kindstr = ' ({})'.format(args.kind)
atstr = ''
userargs.insert(0, args.kind)
if args.at is not None:
atstr = '@' + args.at
call = ['dig', '+time=2', '+short'] + userargs
userargs.append(atstr)
proc = subprocess.Popen(call, stdout=subprocess.PIPE)
stdout, _ = proc.communicate()
if proc.wait() != 0:
self.reply(msg, stdout.decode().strip(';').strip())
results = list(filter(bool, stdout.decode().strip().split('\n')))
return
if results:
resultstr = ', '.join(results)
resultstr = 'no records'
self.reply(msg, '{host}{at}{kind}: {results}'.format(host=args.name, at=
    atstr, kind=kindstr, results=resultstr))
