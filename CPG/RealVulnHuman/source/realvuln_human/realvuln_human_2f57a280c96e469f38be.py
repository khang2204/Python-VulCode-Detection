self.render("login.html", msg="")

    def post(self):
        print "POST ", self.request.uri, "\nBODY ", self.request.body
        con = lite.connect('test.db')
        dat = ""
        uname = self.get_argument('username')
        pwd = self.get_argument('password')
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Users WHERE User ='" +
                        uname + "' AND Password ='" + pwd + "'")
            cur_resp = cur.fetchone()
        if not cur_resp:
            dat = "Login Failed"
        else:
            dat = "Login Success, Hello " + str(cur_resp[1])
        self.render("login.html", msg=dat)


class ServerHandler(tornado.web.RequestHandler):
