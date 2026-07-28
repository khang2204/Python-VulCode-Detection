self.end_headers()
    self.wfile.write(content)
    self.wfile.flush()

def do_GET(self):
    self.params = urlparse.parse_qs(urlparse.urlparse(self.path).query)
    self.path = self.path.split('?', 1)[0]
    self.cookie.load(self.headers.get('Cookie', ''))

    if not self.cookie and '/login' == self.path:
        token = ''.join(random.sample(string.ascii_letters + string.digits, 20))
        self.cookie.load('SESSIONID={}'.format(token))

    ext = os.path.splitext(self.path)[1]
    if (ext == '' or ext == '.html') and (self.path in self.routes):
        handler = TemplateHandler(self)
        handler.find(self.routes[self.path])
    else:
        handler = StaticHandler()
        handler.find(self.path)
