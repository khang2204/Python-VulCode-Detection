def _url_read_json(self, url, **kwargs):...
logging.warn('url_read_json(%s, %s)', url[:500], str(kwargs)[:500])
if not self._requests:
return None
kwargs.pop('stream', None)
for i, n in enumerate(self._requests):
if n[0] == url:
self.fail('Unknown request %s' % url)
data = self._requests.pop(i)
if len(data) != 3:
self.fail('Expected json request, got normal data; %s' % url)
_, expected_kwargs, result = data
if callable(expected_kwargs):
expected_kwargs(kwargs)
self.assertEqual(expected_kwargs, kwargs)
if result is not None:
return result
return None
