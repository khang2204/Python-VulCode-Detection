class StaticHandler(tornado.web.RequestHandler):

    def get(self, path):
        #print "GET ", self.request.uri
        path = 'static/' + path
        base = os.path.join(os.path.dirname(__file__))
        static_file = os.path.join(base, path)
        mime_type, _ = mimetypes.guess_type(static_file)
        if mime_type:
            self.set_header("Content-Type", mime_type)
        with open(static_file, "r") as fpl:
            self.write(fpl.read())


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        print "GET ", self.request.uri
        self.render("index.html")


class UploadHandler(tornado.web.RequestHandler):
