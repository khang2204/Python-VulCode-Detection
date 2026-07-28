return "/vulnpy/{}/{}".format(name, trigger)


def get_trigger_view(name, trigger):
    def _root_view():
        user_input = _get_user_input(request)
        trigger_func = get_trigger(name, trigger)

        if trigger_func:
            trigger_func(user_input)
        template = get_template("{}.html".format(name))

        if name == "xss" and trigger == "raw":
            template += "<p>XSS: " + user_input + "</p>"

        return template

    return _root_view


def generate_root_urls(app):
