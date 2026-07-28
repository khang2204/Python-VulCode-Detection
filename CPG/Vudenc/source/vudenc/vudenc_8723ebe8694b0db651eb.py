import os.path
import datetime
import tornado.ioloop
import tornado.web
import motor.motor_tornado
import crawl
import slugify
import bleach
import bs4
from copy import deepcopy
from tornado import gen
from tornado import escape
from tornado.options import define, options, parse_command_line
import sys
define('port', default=8888, help='run on the given port', type=int)
define('debug', default=True, help='run in debug mode')
define('title', default='The Newsreel')
@property...
return self.settings['db']
