def _call(self, msg, args, errorSink=None):...
pingcmd = ['ping6' if args.ipv6 else 'ping']
if args.alot:
count = 20
count = 5
pingcmd.append('-c{0:d}'.format(count))
proc = subprocess.Popen(pingcmd + self.pingargs + [args.host], stderr=
    subprocess.PIPE, stdout=subprocess.PIPE)
out, err = proc.communicate()
if proc.wait() != 0:
message = err.decode().strip()
lines = out.decode().strip().split('\n')
if not message:
packetinfo = self.packetline.match(lines[3])
self.reply(msg, 'unknown error, timeout/blocked?')
self.reply(msg, 'error: {0}'.format(message))
rttinfo = self.rttline.match(lines[4])
if not packetinfo or not rttinfo:
self.reply(msg, 'unknown error, unable to parse ping output, dumping to stdout'
    )
packetinfo = packetinfo.groups()
print(out.decode())
rttinfo = rttinfo.group(1).split('/')
message = (
    '{host}: {recv}/{sent} pckts., {loss}% loss, rtt ↓/-/↑/↕ = {rttmin}/{rttavg}/{rttmax}/{rttmdev}, time {time}ms'
    .format(host=args.host, sent=int(packetinfo[0]), recv=int(packetinfo[1]
    ), loss=int(packetinfo[3]), rttmin=rttinfo[0], rttavg=rttinfo[1],
    rttmax=rttinfo[2], rttmdev=rttinfo[3], time=int(packetinfo[4])))
self.reply(msg, 'malformatted ping output, dumping to stdout')
self.reply(msg, message)
print(out.decode())
return
