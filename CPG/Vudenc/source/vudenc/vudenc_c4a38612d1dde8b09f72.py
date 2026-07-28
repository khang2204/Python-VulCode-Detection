@tornado.web.asynchronous...
def invoke_404():...
self.set_status(404, 'Not Found')
self._headers = tornado.httputil.HTTPHeaders()
self.add_header('Content-Length', '0')
self.flush()
return
