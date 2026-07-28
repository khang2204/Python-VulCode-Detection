def _url_open(self, url, **kwargs):...
logging.warn('url_open(%s, %s)', url[:500], str(kwargs)[:500])
if not self._requests:
return None
kwargs.pop('stream', None)
for i, n in enumerate(self._requests):
if n[0] == url:
self.fail('Unknown request %s' % url)
data = self._requests.pop(i)
if len(data) != 4:
self.fail('Expected normal request, got json data; %s' % url)
_, expected_kwargs, result, headers = data
if callable(expected_kwargs):
expected_kwargs(kwargs)
self.assertEqual(expected_kwargs, kwargs)
if result is not None:
return make_fake_response(result, url, headers)
return None
