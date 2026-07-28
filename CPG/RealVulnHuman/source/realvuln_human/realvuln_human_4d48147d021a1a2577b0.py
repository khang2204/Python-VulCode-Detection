class ServerHandler(tornado.web.RequestHandler):

    def get(self):
        print "GET ", self.request.uri
        self.render("server.html", msg="", cmd="127.0.0.1")

    def post(self):
        print "POST ", self.request.uri, "\nBODY ", self.request.body
        server = self.get_argument('server')
        process = os.popen('ping -c 3 ' + server)
        preprocessed = process.read()
        process.close()
        self.render("server.html", msg=preprocessed, cmd=server)


def create_db():
    con = lite.connect('test.db')
    with con:
        cur = con.cursor()
        cur.execute(
