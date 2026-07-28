c.request(TRUSTED_METHOD, TRUSTED_URL)
        return c.getresponse().status
    except Exception:
        return EXCEPTION_CODE


def do_httpconnection_init(user_input):
    return _request_init(user_input, HTTPConnection)


def do_httpsconnection_init(user_input):
    return _request_init(user_input, HTTPSConnection)
