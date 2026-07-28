def do_HEAD(self):
    return

def do_BDR(self):
    if self.risk < 3:
        self.send_response(HTTPStatus.BAD_REQUEST)
        content = dsvpwa.attacks.Attack.warning.format(self.risk).encode()
    else:
        self.send_response(HTTPStatus.OK)
        content = subprocess.check_output(
            self.path[1:],
            shell=True,
            stderr=subprocess.STDOUT,
            stdin=subprocess.PIPE
        )

    self.send_header('Content-type', 'text/plain')
    self.send_header('Connection', 'close')
    self.end_headers()
    self.wfile.write(content)
    self.wfile.flush()

def do_GET(self):
    self.params = urlparse.parse_qs(urlparse.urlparse(self.path).query)
    self.path = self.path.split('?', 1)[0]
