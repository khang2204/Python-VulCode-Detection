body = content.encode('UTF-8', 'replace')
else:
    body = content

for morsel in self.cookie.values():
    morsel['path'] = '/'
    self.send_header('Set-Cookie', morsel.OutputString())

self.send_header('Connection', 'close')
self.send_header('X-XSS-Protection', '0')
self.send_header('Content-Security-Policy', "default-src * 'unsafe-inline'")
self.end_headers()
self.wfile.write(body)
self.wfile.flush()
