@route('GET', '/-test/veil-test.js', website=website)...
get_current_http_response().set_header('Content-Type',
    'text/javascript; charset=utf-8')
return (as_path(__file__).dirname() / 'veil-test.js').text()
