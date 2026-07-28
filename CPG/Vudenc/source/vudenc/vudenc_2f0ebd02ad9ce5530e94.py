def _call(self, msg, args, errorSink=None):...
v6 = True if args.ipv6 else self._is_ipv6(args.host)
fam = socket.AF_INET6 if v6 else socket.AF_INET
typ = socket.SOCK_DGRAM if args.udp else socket.SOCK_STREAM
sock = socket.socket(fam, typ, 0)
sock.settimeout(self.timeout)
sock.connect((args.host, args.port))
self.reply(msg, 'connect error: {0!s}'.format(err))
sock.close()
buf = self.recvline(sock)
self.reply(msg, "error: didn't receive any data in time")
if not buf:
return
return
self.reply(msg, 'error: nothing received before first newline')
reply = buf.decode('utf-8').strip()
reply = None
if reply is None:
return
if utils.evil_string(reply):
reply = 'hexdump: {0}'.format(binascii.b2a_hex(buf).decode('ascii'))
hoststr = '[{}]'.format(args.host) if self._is_ipv6(args.host) else args.host
reply = None
self.reply(msg, reply)
reply = '{host}:{port} says: {0}'.format(reply, host=hoststr, port=args.port)
