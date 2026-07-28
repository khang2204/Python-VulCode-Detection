import re
import tornado
from bzs import files
from bzs import const
from bzs import users
from bzs import preproc
SUPPORTED_METHODS = ['GET', 'HEAD']
@tornado.web.asynchronous...
future = tornado.concurrent.Future()
self.set_status(404, 'Not Found')
self.set_status(200, 'OK')
def get_index_html_async():...
self._headers = tornado.httputil.HTTPHeaders()
self._headers = tornado.httputil.HTTPHeaders()
file_data = files.get_static_data('./static/home.html')
self.add_header('Content-Length', '0')
self.add_header('Cache-Control', 'max-age=0')
working_user = users.get_user_by_cookie(self.get_cookie('user_active_login',
    default=''))
self.flush()
self.add_header('Connection', 'close')
file_data = preproc.preprocess_webpage(file_data, working_user)
return None
self.add_header('Content-Type', 'text/html')
future.set_result(file_data)
self.add_header('Content-Length', str(len(file_data)))
tornado.ioloop.IOLoop.instance().add_callback(get_index_html_async)
self.write(file_data)
file_data = yield future
self.flush()
self.finish()
return self
