@mock_connection
def _urlopen(urlopen_func, arg):
    try:
        return urlopen_func(arg).getcode()
    except Exception:
        return EXCEPTION_CODE


def do_legacy_urlopen(user_input):
    """
    PY2: urllib.urlopen
    PY3: urllib.request.urlopen (fallback only, not intended for use)
    """
    return _urlopen(legacy_urlopen, user_input)


def do_urlopen_str(user_input):
    """
    PY2: urllib2.urlopen
    PY3: urllib.request.urlopen
    """
    return _urlopen(urlopen, user_input)
