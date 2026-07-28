def do_httpsconnection_request_url(user_input):
    return _request(user_input, HTTPSConnection, "request", True)


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
