def get(self):...
if not enable_authentication:
self.redirect('/')
self.write(
    '<html><head><title>Liked Saved Downloader</title><link rel="stylesheet" type="text/css" href="webInterfaceNoAuth/index.css"></head><body><h1>Login Required</h1><form action="/login" method="post">Name: <input type="text" name="name"><br />Password: <input type="password" name="password">{}<br /><input type="submit" value="Sign in"></form></body></html>'
    .format(self.xsrf_form_html()))
