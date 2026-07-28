read_file.close()
        self.write(content)


class SearchHandler(tornado.web.RequestHandler):

    def get(self):
        print "GET ", self.request.uri
        query = self.get_argument("q", default="Query")
        self.set_header('X-XSS-Protection', '0')
        self.render("search.html", query=query, link=query)


class UsersHandler(tornado.web.RequestHandler):

    def get(self):
        print "GET ", self.request.uri
        self.render("login.html", msg="")

    def post(self):
        print "POST ", self.request.uri, "\nBODY ", self.request.body
