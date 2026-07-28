def _rest_call(self, url, method='GET', body=None, headers=None, silent=False):...
request_headers = headers.copy() if headers else {}
request_headers.update(self._default_headers)
request_url = self._build_url(url)
do_request = getattr(self._conn, method.lower())
if not silent:
LOG.debug('REST call: %s %s. Headers: %s. Body: %s', method, request_url,
    request_headers, self._mask_password(body))
ts = time.time()
result = do_request(request_url, data=body, headers=request_headers)
te = time.time()
if not silent:
LOG.debug('REST call: %s %s. Response: %s. Took %2.4f', method, request_url,
    result.json() if result.content else '', te - ts)
self._validate_result(result, RESTClient._VERB_RESP_CODES[method.lower()], 
    _('%(verb)s %(url)s') % {'verb': method, 'url': request_url}, silent=silent
    )
return result
