else:
            request_method(user_input, TRUSTED_URL)
        if method_name == "putrequest":
            c.endheaders()

        return c.getresponse().status
    except Exception:
        return EXCEPTION_CODE


def do_httpconnection_request_url(user_input):
    return _request(user_input, HTTPConnection, "request", True)


def do_httpconnection_request_method(user_input):
    return _request(user_input, HTTPConnection, "request", False)


def do_httpconnection_putrequest_url(user_input):
    return _request(user_input, HTTPConnection, "putrequest", True)
