import os.path
import tornado.web
import tornado.httpserver
import tornado.options
import tornado.ioloop
from config.MockConfigDAO import MockConfigDAO
cfgDAO = MockConfigDAO()
from tornado.options import define, options
define('port', default=8080, help='Server port', type=int)
""" Configure server """
def __init__(self):...
handlers = [('/', ReqHandler), ('/login', LoginHandler), ('/logout',
    LogoutHandler), ('/config', ConfigHandler), ('/(\\w+)', ReqHandler)]
mainDir = os.path.dirname(__file__)
settings = dict(xsrf_cookie=True, cookie_secret=
    'bls9+x7PT5GIbaBuKzsGOecL9SG7KUmEh6rNbMYTpfk=', login_url='/login',
    template_path=os.path.join(mainDir, 'templates/myStyle'), static_path=
    os.path.join(mainDir, 'templates/myStyle/static'))
tornado.web.Application.__init__(self, handlers, **settings)
""" This class specifies how we store the user identity """
def get_current_user(self):...
return self.get_secure_cookie('user')
