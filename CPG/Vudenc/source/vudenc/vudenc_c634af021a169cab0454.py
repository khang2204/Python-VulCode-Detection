def JsonFromFuture(future):...
response = future.result()
if response.status_code == requests.codes.server_error:
_RaiseExceptionForData(response.json())
response.raise_for_status()
if response.text:
return response.json()
return None
