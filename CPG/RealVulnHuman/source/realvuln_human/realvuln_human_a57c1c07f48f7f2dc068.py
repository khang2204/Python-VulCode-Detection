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


def do_urlopen_obj(user_input):
    """
    Same as urlopen_str, but first creates a request object.
    """
    try:
        req = Request(user_input)
    except Exception:
        req = None
