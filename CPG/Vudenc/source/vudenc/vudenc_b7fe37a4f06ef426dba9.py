def make_app():...
randomGenerator = random.SystemRandom()
cookieSecret = str(randomGenerator.getrandbits(128))
return tornado.web.Application([('/', HomeHandler), ('/login', LoginHandler
    ), ('/logout', LogoutHandler), ('/settings', SettingsHandler), (
    '/runScriptWebSocket', RunScriptWebSocket), (
    '/randomImageBrowserWebSocket', RandomImageBrowserWebSocket), (
    '/webInterface/(.*)', AuthedStaticHandler, {'path': 'webInterface'}), (
    '/output/(.*)', AuthedStaticHandler, {'path': settings.settings[
    'Output_dir']}), ('/webInterfaceNoAuth/(.*)', tornado.web.
    StaticFileHandler, {'path': 'webInterfaceNoAuth'})], xsrf_cookies=True,
    cookie_secret=cookieSecret, login_url='/login')
