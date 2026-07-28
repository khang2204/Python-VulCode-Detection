def do_httpsconnection_request_method(user_input):
    return _request(user_input, HTTPSConnection, "request", False)


def do_httpsconnection_putrequest_url(user_input):
    return _request(user_input, HTTPSConnection, "putrequest", True)


def do_httpsconnection_putrequest_method(user_input):
    return _request(user_input, HTTPSConnection, "putrequest", False)


@mock_connection
def _request_init(user_input, connection_class):
    try:
        c = connection_class(user_input)
        c.request(TRUSTED_METHOD, TRUSTED_URL)
        return c.getresponse().status
    except Exception:
        return EXCEPTION_CODE
