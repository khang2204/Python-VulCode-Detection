import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
define('port', default=8000, help='run on specified port', type=int)
def get_current_user(self):...
return self.get_secure_cookie('username')
