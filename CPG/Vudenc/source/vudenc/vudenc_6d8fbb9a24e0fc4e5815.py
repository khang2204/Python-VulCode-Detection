import logging
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options
import application
import handlers
import settings
import beacon
define('port', default=4000, help='run on the given port', type=int)
define('develop', default=False, help='Run in develop environment', type=bool)
redirect_uri = settings.redirect_uri
settings = {'debug': False, 'cookie_secret': settings.cookie_secret,
    'login_url': '/login', 'google_oauth': {'key': settings.google_key,
    'secret': settings.google_secret}, 'contact_person':
    'mats.dahlberg@scilifelab.se', 'redirect_uri': redirect_uri,
    'template_path': 'templates/'}
def __init__(self, settings):...
self.declared_handlers = [('/static/(.*)', tornado.web.StaticFileHandler, {
    'path': 'static/'}), ('/(favicon.ico)', tornado.web.StaticFileHandler,
    {'path': 'static/img/'}), ('/release/(?P<dataset>[^\\/]+)/(?P<file>.*)',
    handlers.AuthorizedStaticNginxFileHanlder, {'path': '/release-files/'}),
    ('/login', handlers.LoginHandler), ('/logout', handlers.LogoutHandler),
    ('/api/countries', application.CountryList), ('/api/users/me',
    application.GetUser), ('/api/datasets', application.ListDatasets), (
    '/api/datasets/(?P<dataset>[^\\/]+)', application.GetDataset), (
    '/api/datasets/(?P<dataset>[^\\/]+)/log/(?P<event>[^\\/]+)',
    application.LogEvent), ('/api/datasets/(?P<dataset>[^\\/]+)/logo',
    application.ServeLogo), ('/api/datasets/(?P<dataset>[^\\/]+)/files',
    application.DatasetFiles), (
    '/api/datasets/(?P<dataset>[^\\/]+)/sample_set', application.SampleSet),
    ('/api/datasets/(?P<dataset>[^\\/]+)/users', application.DatasetUsers),
    ('/api/datasets/(?P<dataset>[^\\/]+)/users/(?P<email>[^\\/]+)/request',
    application.RequestAccess), (
    '/api/datasets/(?P<dataset>[^\\/]+)/users/(?P<email>[^\\/]+)/approve',
    application.ApproveUser), (
    '/api/datasets/(?P<dataset>[^\\/]+)/users/(?P<email>[^\\/]+)/revoke',
    application.RevokeUser), ('/api/query', beacon.Query), ('/api/info',
    beacon.Info), ('/query', beacon.Query), ('/info', tornado.web.
    RedirectHandler, {'url': '/api/info'}), ('.*', application.Home)]
self.oauth_key = settings['google_oauth']['key']
tornado.web.Application.__init__(self, self.declared_handlers, **settings)
if __name__ == '__main__':
tornado.log.enable_pretty_logging()
tornado.options.parse_command_line()
if options.develop:
settings['debug'] = True
application = Application(settings)
settings['develop'] = True
application.listen(options.port)
logging.getLogger().setLevel(logging.DEBUG)
http_server = tornado.httpserver.HTTPServer(application)
ioloop = tornado.ioloop.IOLoop.instance()
ioloop.start()
