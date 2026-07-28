def do_urlopen_str(user_input):
    """
    PY2: urllib2.urlopen
    PY3: urllib.request.urlopen
    """
    return _urlopen(urlopen, user_input)


def do_urlopen_obj(user_input):
    """
    Same as urlopen_str, but first creates a request object.
    """
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
