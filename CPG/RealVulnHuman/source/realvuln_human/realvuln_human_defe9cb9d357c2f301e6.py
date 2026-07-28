def do_httpconnection_request_method(user_input):
    return _request(user_input, HTTPConnection, "request", False)


def do_httpconnection_putrequest_url(user_input):
    return _request(user_input, HTTPConnection, "putrequest", True)


def do_httpconnection_putrequest_method(user_input):
    return _request(user_input, HTTPConnection, "putrequest", False)


def do_httpsconnection_request_url(user_input):
    return _request(user_input, HTTPSConnection, "request", True)


def do_httpsconnection_request_method(user_input):
    return _request(user_input, HTTPSConnection, "request", False)
