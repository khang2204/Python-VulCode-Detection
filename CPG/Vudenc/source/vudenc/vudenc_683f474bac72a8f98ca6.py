def _local_server_get(url, session):...
"""docstring"""
request = HttpRequest()
request.method = 'GET'
request.session = session
view, args, kwargs = resolve(url)
response = view(request, *args, **kwargs)
return response.content
