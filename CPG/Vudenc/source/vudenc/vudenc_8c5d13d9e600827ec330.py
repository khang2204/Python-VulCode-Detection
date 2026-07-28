import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.httpclient
import tornado.httpserver
import tornado.gen
import os
from datetime import datetime
import ContentConverter
def get(self):...
allPosts = ContentConverter.getAllPostsList()
self.render('templates/Home.html', allPosts=allPosts)
def get(self, request):...
contentTitle = 'Blog: ' + request
renderedBody = ContentConverter.getRenderedBody(request)
if not renderedBody:
renderedBody = "<p>The post under '{}' does not exist.</p>".format(request)
self.render('templates/BlogPost.html', title=contentTitle, postBody=
    renderedBody)
def make_app():...
return tornado.web.Application([('/', HomeHandler), ('/blog/(.*)',
    BlogHandler), ('/webResources/(.*)', tornado.web.StaticFileHandler, {
    'path': 'webResources'})], xsrf_cookies=True, cookie_secret=
    'this is my org blog')
