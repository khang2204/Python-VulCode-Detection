def make_app():...
return tornado.web.Application([('/', HomeHandler), ('/blog/(.*)',
    BlogHandler), ('/webResources/(.*)', tornado.web.StaticFileHandler, {
    'path': 'webResources'})], xsrf_cookies=True, cookie_secret=
    'this is my org blog')
