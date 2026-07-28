@template_utility...
request = request or get_current_http_request()
assert request._xsrf_token is not None
return request._xsrf_token
