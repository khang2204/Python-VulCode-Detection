def get_routes():...
routes = [('/bootstrap', BootstrapHandler), ('/bot_code', BotCodeHandler),
    ('/swarming/api/v1/bot/bot_code/<version:[0-9a-f]{40}>', BotCodeHandler
    ), ('/swarming/api/v1/bot/event', BotEventHandler), (
    '/swarming/api/v1/bot/handshake', BotHandshakeHandler), (
    '/swarming/api/v1/bot/poll', BotPollHandler), (
    '/swarming/api/v1/bot/server_ping', ServerPingHandler), (
    '/swarming/api/v1/bot/task_update', BotTaskUpdateHandler), (
    '/swarming/api/v1/bot/task_update/<task_id:[a-f0-9]+>',
    BotTaskUpdateHandler), ('/swarming/api/v1/bot/task_error',
    BotTaskErrorHandler), (
    '/swarming/api/v1/bot/task_error/<task_id:[a-f0-9]+>', BotTaskErrorHandler)
    ]
return [webapp2.Route(*i) for i in routes]
