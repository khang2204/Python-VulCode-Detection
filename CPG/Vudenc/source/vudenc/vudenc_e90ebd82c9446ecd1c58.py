def main():...
web_app = tornado.web.Application([('^/$', module_index.MainframeHandler),
    ('/static/.*', module_static.StaticHandler), ('^/home', module_home.
    HomeHandler), ('^/files/?()$', module_files.FilesListHandler), (
    '^/files/list/(.*)', module_files.FilesListHandler), (
    '^/files/download/(.*)/(.*)/?$', module_files.FilesDownloadHandler), (
    '^/files/upload/(.*)/(.*)$', module_files.FilesUploadHandler), (
    '^/files/operation/?', module_files.FilesOperationHandler), ('.*',
    module_error404.Error404Handler)], xsrf_cookies=False)
web_sockets = tornado.netutil.bind_sockets(const.get_const('server-port'),
    family=socket.AF_INET)
if const.get_const('server-threads') > 1:
if hasattr(os, 'fork'):
web_server = tornado.httpserver.HTTPServer(web_app, xheaders=True)
tornado.process.fork_processes(const.get_const('server-threads') - 1)
web_server.add_sockets(web_sockets)
tornado.ioloop.IOLoop.instance().start()
return
