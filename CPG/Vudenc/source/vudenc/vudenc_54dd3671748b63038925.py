def __call__(self, environ, start_response):...
path = decode_path_info(environ.get('PATH_INFO', ''))
if self.autorefresh:
static_file = self.find_file(path)
static_file = self.files.get(path)
if static_file is None:
return self.application(environ, start_response)
return self.serve(static_file, environ, start_response)
