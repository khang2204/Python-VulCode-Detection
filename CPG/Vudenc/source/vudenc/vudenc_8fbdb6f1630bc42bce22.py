@staticmethod...
response = static_file.get_response(environ['REQUEST_METHOD'], environ)
status_line = '{} {}'.format(response.status, response.status.phrase)
start_response(status_line, list(response.headers))
if response.file is not None:
file_wrapper = environ.get('wsgi.file_wrapper', FileWrapper)
return []
return file_wrapper(response.file)
