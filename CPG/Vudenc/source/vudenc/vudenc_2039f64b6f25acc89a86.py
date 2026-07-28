@staticmethod...
def SendRequest(data, handler, method, timeout):...
if method == 'POST':
return BaseRequest.session.post(_BuildUri(handler), data=ToUtf8Json(data),
    headers=_HEADERS, timeout=timeout)
if method == 'GET':
return BaseRequest.session.get(_BuildUri(handler), headers=_HEADERS,
    timeout=timeout)
@retries(5, delay=0.5, backoff=1.5)...
if method == 'POST':
return requests.post(_BuildUri(handler), data=ToUtf8Json(data), headers=
    _HEADERS)
if method == 'GET':
return requests.get(_BuildUri(handler), headers=_HEADERS)
if not _CheckServerIsHealthyWithCache():
return _EXECUTOR.submit(DelayedSendRequest, data, handler, method)
return SendRequest(data, handler, method, timeout)
