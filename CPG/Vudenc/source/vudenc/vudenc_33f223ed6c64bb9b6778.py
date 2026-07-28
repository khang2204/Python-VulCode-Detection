import re
import tornado
from bzs import files
from bzs import const
SUPPORTED_METHODS = ['GET', 'HEAD']
@tornado.web.asynchronous...
file_data = files.get_static_data('./static/404.html')
file_data = '404 Not Found'
self.set_status(200, 'OK')
self._headers = tornado.httputil.HTTPHeaders()
self.add_header('Cache-Control', 'max-age=0')
self.add_header('Connection', 'close')
self.add_header('Content-Type', 'text/html')
self.add_header('Content-Length', str(len(file_data)))
self.write(file_data)
self.flush()
self.finish()
return self
