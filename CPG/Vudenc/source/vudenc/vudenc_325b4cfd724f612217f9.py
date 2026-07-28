@route('POST', '/-test/fail', website=website)...
message = get_http_argument('message')
LOGGER.error(message)
get_executing_test().error = message
