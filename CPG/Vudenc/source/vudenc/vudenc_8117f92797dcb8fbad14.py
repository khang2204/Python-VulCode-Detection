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
