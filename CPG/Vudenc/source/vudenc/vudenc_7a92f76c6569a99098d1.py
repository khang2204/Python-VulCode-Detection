def SendRequest(data, handler, method, timeout):...
if method == 'POST':
return BaseRequest.session.post(_BuildUri(handler), data=ToUtf8Json(data),
    headers=_HEADERS, timeout=timeout)
if method == 'GET':
return BaseRequest.session.get(_BuildUri(handler), headers=_HEADERS,
    timeout=timeout)
