def get_trigger_view(name, trigger):
    async def _view(request):
        user_input = _get_user_input(request)
        trigger_func = get_trigger(name, trigger)

        if trigger_func:
            trigger_func(user_input)

        template = get_template("{}.html".format(name))

        if name == "xss" and trigger == "raw":
            template += "<p>XSS: " + user_input + "</p>"

        return web.Response(text=template, content_type="text/html")

    return _view


def get_root_name(name):
