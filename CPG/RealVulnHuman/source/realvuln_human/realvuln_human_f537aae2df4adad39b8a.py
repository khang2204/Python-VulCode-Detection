(r"/", MainHandler),
            (r"/index.html", MainHandler),
            (r"/search", SearchHandler),
            (r"/login.html", UsersHandler),
            (r"/server.html", ServerHandler),
            (r"/upload", UploadHandler),
            (r"/read", ContentHandler),
        ]
        settings = {
            "template_path": os.path.join(os.path.dirname(__file__), 'templates'),
            "debug": True
        }
        tornado.web.Application.__init__(self, handlers, **settings)


class StaticHandler(tornado.web.RequestHandler):

    def get(self, path):
        #print "GET ", self.request.uri
        path = 'static/' + path
        base = os.path.join(os.path.dirname(__file__))
