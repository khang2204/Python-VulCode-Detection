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


print(encrypt('admin'))

if __name__ == "__main__":
    webServer = HTTPServer(('0.0.0.0', 1337), MyServer)
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
