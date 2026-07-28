@trial_timeout(20)...
"""docstring"""
self.messages_to_wait_for = 20
def send_notifications(_):...
self.session.notifier.notify(NTFY_UPGRADER, NTFY_STARTED, None, None)
self.session.notifier.notify(NTFY_UPGRADER_TICK, NTFY_STARTED, None, None)
self.session.notifier.notify(NTFY_UPGRADER, NTFY_FINISHED, None, None)
self.session.notifier.notify(NTFY_WATCH_FOLDER_CORRUPT_TORRENT, NTFY_INSERT,
    None, None)
self.session.notifier.notify(NTFY_NEW_VERSION, NTFY_INSERT, None, None)
self.session.notifier.notify(NTFY_CHANNEL, NTFY_DISCOVERED, None, None)
self.session.notifier.notify(NTFY_TORRENT, NTFY_DISCOVERED, None, {'a':
    'Invalid character ¡'})
self.session.notifier.notify(NTFY_TORRENT, NTFY_FINISHED, 'a' * 10, None)
self.session.notifier.notify(NTFY_TORRENT, NTFY_ERROR, 'a' * 10,
    'This is an error message')
self.session.notifier.notify(NTFY_MARKET_ON_ASK, NTFY_UPDATE, None, {'a': 'b'})
self.session.notifier.notify(NTFY_MARKET_ON_BID, NTFY_UPDATE, None, {'a': 'b'})
self.session.notifier.notify(NTFY_MARKET_ON_ASK_TIMEOUT, NTFY_UPDATE, None,
    {'a': 'b'})
self.session.notifier.notify(NTFY_MARKET_ON_BID_TIMEOUT, NTFY_UPDATE, None,
    {'a': 'b'})
self.session.notifier.notify(NTFY_MARKET_ON_TRANSACTION_COMPLETE,
    NTFY_UPDATE, None, {'a': 'b'})
self.session.notifier.notify(NTFY_MARKET_ON_PAYMENT_RECEIVED, NTFY_UPDATE,
    None, {'a': 'b'})
self.session.notifier.notify(NTFY_MARKET_ON_PAYMENT_SENT, NTFY_UPDATE, None,
    {'a': 'b'})
self.session.notifier.notify(SIGNAL_RESOURCE_CHECK, SIGNAL_LOW_SPACE, None, {})
self.session.notifier.notify(NTFY_CREDIT_MINING, NTFY_ERROR, None, {
    'message': 'Some credit mining error'})
self.session.notifier.notify(NTFY_TUNNEL, NTFY_REMOVE, Circuit(1234, None),
    'test')
self.session.lm.api_manager.root_endpoint.events_endpoint.on_tribler_exception(
    'hi')
self.socket_open_deferred.addCallback(send_notifications)
return self.events_deferred
