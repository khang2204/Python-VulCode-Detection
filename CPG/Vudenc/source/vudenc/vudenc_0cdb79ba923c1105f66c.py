def get(self, request):...
contentTitle = 'Blog: ' + request
renderedBody = ContentConverter.getRenderedBody(request)
if not renderedBody:
renderedBody = "<p>The post under '{}' does not exist.</p>".format(request)
self.render('templates/BlogPost.html', title=contentTitle, postBody=
    renderedBody)
