@wraps(view)...
response = make_response(view(*args, **kwargs))
response.headers['Last-Modified'] = datetime.now()
response.headers['Cache-Control'
    ] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
response.headers['Pragma'] = 'no-cache'
response.headers['Expires'] = '-1'
return response
