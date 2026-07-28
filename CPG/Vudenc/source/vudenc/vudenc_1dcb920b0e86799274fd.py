@route('GET', '/-test/jquery.js', website=website)...
get_current_http_response().set_header('Content-Type',
    'text/javascript; charset=utf-8')
return (as_path(__file__).dirname() / 'jquery.js').text()
