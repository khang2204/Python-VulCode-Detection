def app_css_hash(self):...
if not hasattr(self, '_app_css_hash'):
self._app_css_hash = hashlib.sha1(open(os.path.join(str(app_root),
    'datasette/static/app.css')).read().encode('utf8')).hexdigest()[:6]
return self._app_css_hash
