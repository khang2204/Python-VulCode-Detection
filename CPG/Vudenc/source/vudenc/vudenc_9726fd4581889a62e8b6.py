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
