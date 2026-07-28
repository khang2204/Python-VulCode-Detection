def getFields(environ):...
"""docstring"""
data_env = environ.copy()
data_env['QUERY_STRING'] = ''
data = cgi.FieldStorage(fp=environ['wsgi.input'], environ=data_env,
    keep_blank_values=True)
return data
