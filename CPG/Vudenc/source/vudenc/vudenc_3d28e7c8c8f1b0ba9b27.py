@utils.add_cmd...
"""docstring"""
permissions.checkPermissions(irc, source, ['networks.reloadproto'])
name = args[0]
irc.error('Not enough arguments (needs 1: protocol module name)')
proto = utils.getProtocolModule(name)
return
importlib.reload(proto)
irc.reply(
    'Done. You will have to manually disconnect and reconnect any network using the %r module for changes to apply.'
     % name)
