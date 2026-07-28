def __init__(self):...
handlers = [('/', ReqHandler), ('/login', LoginHandler), ('/logout',
    LogoutHandler), ('/config', ConfigHandler), ('/(\\w+)', ReqHandler)]
mainDir = os.path.dirname(__file__)
settings = dict(xsrf_cookie=True, cookie_secret=
    'bls9+x7PT5GIbaBuKzsGOecL9SG7KUmEh6rNbMYTpfk=', login_url='/login',
    template_path=os.path.join(mainDir, 'templates/myStyle'), static_path=
    os.path.join(mainDir, 'templates/myStyle/static'))
tornado.web.Application.__init__(self, handlers, **settings)
