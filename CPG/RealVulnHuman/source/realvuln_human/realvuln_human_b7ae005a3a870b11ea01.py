generate_trigger_urls(app)


def _set_response(resp, path):
    """
    Set the response body and Content-Type
    """
    resp.text = get_template(path)
    resp.content_type = "text/html"


def _set_xss_response(resp, path, user_input):
    template = get_template(path)
    template += "<p>XSS: " + user_input + "</p>"

    resp.text = template
    resp.content_type = "text/html"
