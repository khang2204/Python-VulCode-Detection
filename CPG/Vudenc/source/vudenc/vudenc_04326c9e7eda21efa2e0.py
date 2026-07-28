@retries(5, delay=0.5, backoff=1.5)...
if method == 'POST':
return requests.post(_BuildUri(handler), data=ToUtf8Json(data), headers=
    _HEADERS)
if method == 'GET':
return requests.get(_BuildUri(handler), headers=_HEADERS)
