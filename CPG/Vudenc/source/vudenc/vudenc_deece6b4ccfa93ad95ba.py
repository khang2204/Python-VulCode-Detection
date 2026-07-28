def record_call(self, request, **kwargs):...
verb = request.method.lower()
checked_kwargs = copy.copy(kwargs)
if 'allow_redirects' in checked_kwargs:
for attr in ['url', 'body']:
checked_kwargs[attr] = getattr(request, attr, None)
checked_kwargs['headers'] = copy.copy(request.headers)
for header in ['Accept-Encoding', 'User-Agent', 'Connection',
if header in checked_kwargs['headers']:
checked_kwargs['headers'] = request.headers
method = getattr(self._record, verb)
method(**checked_kwargs)
