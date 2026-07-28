def main():...
parse_command_line()
db = motor.motor_tornado.MotorClient().news
collection = db.articles
app = tornado.web.Application([('/', MainHandler), ('/post/(.+)',
    PostHandler), ('/new', PostNewHandler)], cookie_secret=
    '__THERE_IS_NO_SECRET_COOKIE__', template_path=os.path.join(os.path.
    dirname(__file__), 'templates'), static_path=os.path.join(os.path.
    dirname(__file__), 'static'), xsrf_cookies=True, debug=options.debug,
    db=db, collection=collection)
print('Listening on http://localhost:{}'.format(options.port))
app.listen(options.port)
tornado.ioloop.IOLoop.current().start()
