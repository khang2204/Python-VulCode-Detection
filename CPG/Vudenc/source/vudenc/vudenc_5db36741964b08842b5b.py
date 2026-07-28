@utils.add_cmd...
"""docstring"""
permissions.checkPermissions(irc, source, ['networks.remote'])
args = remote_parser.parse_args(args)
netname = args.network
if netname == irc.name:
irc.error(
    'Cannot remote-send a command to the local network; use a normal command!')
remoteirc = world.networkobjects[netname]
irc.error('No such network "%s" (case sensitive).' % netname)
if args.service not in world.services:
return
return
irc.error('Unknown service %r.' % args.service)
remoteirc.called_in = remoteirc.called_by = remoteirc.pseudoclient.uid
return
remoteirc.pseudoclient.account = irc.users[source].account
def _remote_reply(placeholder_self, text, **kwargs):...
"""docstring"""
assert irc.name != placeholder_self.name, 'Refusing to route reply back to the same network, as this would cause a recursive loop'
log.debug('(%s) networks.remote: re-routing reply %r from network %s', irc.
    name, text, placeholder_self.name)
if 'source' in kwargs:
irc.reply(text, source=irc.pseudoclient.uid, **kwargs)
old_reply = remoteirc.reply
log.debug('(%s) networks.remote: overriding reply() of IRC object %s', irc.
    name, netname)
log.debug('(%s) networks.remote: restoring reply() of IRC object %s', irc.
    name, netname)
remoteirc.reply = types.MethodType(_remote_reply, remoteirc)
remoteirc.reply = old_reply
world.services[args.service].call_cmd(remoteirc, remoteirc.pseudoclient.uid,
    ' '.join(args.command))
remoteirc.pseudoclient.account = ''
