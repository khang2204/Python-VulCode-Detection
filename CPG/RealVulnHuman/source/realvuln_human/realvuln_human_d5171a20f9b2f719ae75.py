response.append("<p>XSS: {}</p>".format(user_input))

    response.append(get_template("{}.html".format(name)))
    headers = [("Content-Type", "text/html")]

    # This makes the app vulnerable to cache control missing, since both no-cache and
    # no-store are missing
    headers.append(("Cache-Control", "public"))
    # This makes the app vulnerable to X-XSS-Protection disabled
    headers.append(("X-XSS-Protection", "0"))
    headers.append(("Strict-Transport-Security", "max-age=0"))

    start_response("200 OK", headers)

    return [ensure_binary(s) for s in response]


class NotFound(Exception):
    pass
