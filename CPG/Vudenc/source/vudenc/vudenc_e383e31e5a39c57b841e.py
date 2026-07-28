def _remote_reply(placeholder_self, text, **kwargs):...
"""docstring"""
assert irc.name != placeholder_self.name, 'Refusing to route reply back to the same network, as this would cause a recursive loop'
log.debug('(%s) networks.remote: re-routing reply %r from network %s', irc.
    name, text, placeholder_self.name)
if 'source' in kwargs:
irc.reply(text, source=irc.pseudoclient.uid, **kwargs)
