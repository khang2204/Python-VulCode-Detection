iv = enc[0:AES.block_size]
    encd = enc[AES.block_size:]
    aes = AES.new(KEY, AES.MODE_CBC, iv)
    return unpad(aes.decrypt(encd), AES.block_size).decode('utf-8')

def do_GET(self):
    cookies = SimpleCookie(self.headers.get('Cookie'))
    if cookies.get('session_id'):
        try:
            username = self.decrypt(cookies.get('session_id').value) # regex and escaped all inputs
        except:
            self.send_response(500)
            return
    else:
        username = 'Anonymous'
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(bytes("Hello", "utf-8"))
    self.wfile.write(bytes("", "utf-8"))
    self.wfile.write(bytes("Hello %s" % username, "utf-8")) # needs encoding
    self.wfile.write(bytes("", "utf-8"))
