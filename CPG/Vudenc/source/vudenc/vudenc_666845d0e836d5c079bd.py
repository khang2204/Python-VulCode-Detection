def set_default_headers(self):...
"""docstring"""
self.request.start_time = datetime_now()
self.xsrf_token
self.set_header('Server', 'globaleaks')
self.set_header('X-Content-Type-Options', 'nosniff')
self.set_header('X-XSS-Protection', '1; mode=block')
self.set_header('Cache-control', 'no-cache, no-store, must-revalidate')
self.set_header('Pragma', 'no-cache')
self.set_header('Expires', '-1')
self.set_header('X-Robots-Tag', 'noindex')
if not GLSetting.devel_mode:
self.set_header('X-Frame-Options', 'deny')
lang = self.request.headers.get('GL-Language', None)
if not lang:
lang = GLSetting.memory_copy.default_language
self.request.language = lang
