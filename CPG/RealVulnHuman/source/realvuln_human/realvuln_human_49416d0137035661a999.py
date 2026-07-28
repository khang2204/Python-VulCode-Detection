from http.server import BaseHTTPRequestHandler, HTTPServer
from Encrypt import Encrypt
from Username import Username


class MyServer(BaseHTTPRequestHandler):

    def get(self):
        cookies = SimpleCookie(self.headers.get('Cookie'))
        if cookies.get('username'):
            Username.pickle()
            # username = pickle.loads(base64.b64decode(cookies.get('username').value))
            # Issue:B301:blacklist Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data
            # Vulnerable code below: Calls pickle.loads on user supplied info
            # No signature present or anything preventing the sending of a malicious pickle object
            # This would enable code execution

        else:
            username='stranger'
            self.send_response(200)
            self.send_header("Content-type", "text/html")
