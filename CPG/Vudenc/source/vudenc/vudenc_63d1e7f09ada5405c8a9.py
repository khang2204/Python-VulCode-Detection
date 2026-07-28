def launch():...
server_settings = {'static_path': os.path.join(os.path.dirname(__file__),
    './static'), 'template_path': './server/templates', 'login_url':
    '/login', 'cookie_secret': os.urandom(24), 'xsrf_cookies': True}
handlers = [('/', IndexController), ('/report', ReportController), (
    '/create', ReportController.NewReportController), ('/login',
    LoginController), ('/logout', LoginController.LogoutController)]
application = tornado.web.Application(handlers, **server_settings)
http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(options.port)
tornado.ioloop.IOLoop.instance().start()
