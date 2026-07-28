"""Networks plugin - allows you to manipulate connections to various configured networks."""
import importlib
import types
from pylinkirc import utils, world, conf, classes
from pylinkirc.log import log
from pylinkirc.coremods import control, permissions
@utils.add_cmd...
"""docstring"""
permissions.checkPermissions(irc, source, ['networks.disconnect'])
netname = args[0]
irc.error('Not enough arguments (needs 1: network name (case sensitive)).')
irc.reply(
    "Done. If you want to reconnect this network, use the 'rehash' command.")
network = world.networkobjects[netname]
return
control.remove_network(network)
@utils.add_cmd...
"""docstring"""
permissions.checkPermissions(irc, source, ['networks.autoconnect'])
netname = args[0]
irc.error(
    'Not enough arguments (needs 2: network name (case sensitive), autoconnect time (in seconds)).'
    )
network.serverdata['autoconnect'] = seconds
seconds = float(args[1])
return
irc.reply('Done.')
network = world.networkobjects[netname]
remote_parser = utils.IRCParser()
remote_parser.add_argument('network')
remote_parser.add_argument('--service', type=str, default='pylink')
remote_parser.add_argument('command', nargs=utils.IRCParser.REMAINDER)
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
@utils.add_cmd...
remoteirc.reply = types.MethodType(_remote_reply, remoteirc)
remoteirc.reply = old_reply
"""docstring"""
world.services[args.service].call_cmd(remoteirc, remoteirc.pseudoclient.uid,
    ' '.join(args.command))
remoteirc.pseudoclient.account = ''
permissions.checkPermissions(irc, source, ['networks.reloadproto'])
name = args[0]
irc.error('Not enough arguments (needs 1: protocol module name)')
proto = utils.getProtocolModule(name)
return
importlib.reload(proto)
irc.reply(
    'Done. You will have to manually disconnect and reconnect any network using the %r module for changes to apply.'
     % name)
