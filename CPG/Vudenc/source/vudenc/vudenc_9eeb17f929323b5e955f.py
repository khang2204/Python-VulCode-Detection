@app.middleware('response')...
if original_response.status == 404 and request.path.endswith('/'):
path = request.path.rstrip('/')
if request.query_string:
path = '{}?{}'.format(path, request.query_string)
return response.redirect(path)
