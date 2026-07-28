def reply(self, body, status='200 OK', mime='text/html', headers=[]):...
response = [u'HTTP/1.1 ' + status, u'Connection: Keep-Alive', 
    u'Content-Type: ' + mime, u'Content-Length: ' + str(len(body))]
response.extend(headers)
response_str = u'\r\n'.join(response).encode('utf-8')
if self.ok:
self.s.send(response_str + b'\r\n\r\n' + body)
return body
