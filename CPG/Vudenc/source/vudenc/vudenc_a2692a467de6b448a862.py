def set_xsrf_cookie_for_page(route_handler, data):...
if get_current_http_request().is_new_xsrf_token:
if data and '<html' in data.lower():
return data
set_cookie(name='_xsrf', value=xsrf_token())
