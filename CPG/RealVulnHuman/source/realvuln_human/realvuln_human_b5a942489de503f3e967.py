try:
        req = Request(user_input)
    except Exception:
        req = None
    return _urlopen(urlopen, req)


@mock_connection
def _request(user_input, connection_class, method_name, vulnerable_url):
    try:
        c = connection_class(TRUSTED_HOST)

        request_method = getattr(c, method_name)
        if vulnerable_url:
            request_method(TRUSTED_METHOD, user_input)
        else:
            request_method(user_input, TRUSTED_URL)
        if method_name == "putrequest":
            c.endheaders()

        return c.getresponse().status
