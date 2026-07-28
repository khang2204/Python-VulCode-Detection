@route('GET', '/-test/jquery-cookie.js', website=website)...
get_current_http_response().set_header('Content-Type',
    'text/javascript; charset=utf-8')
return (as_path(__file__).dirname() / 'jquery-cookie.js').text()
