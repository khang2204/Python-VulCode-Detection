def make_application() ->tornado.web.Application:...
return tornado.web.Application([('/', CreatePaste), ('/\\+(.*)',
    CreatePaste), ('/show/(.*)', ShowPaste), ('/raw/(.*)', RawPaste), (
    '/remove/(.*)', RemovePaste), ('/static/(.*)', tornado.web.
    StaticFileHandler, {'path': path.static})], template_path=path.template,
    session_factory=database.session_factory)
