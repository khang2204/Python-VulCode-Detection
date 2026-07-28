view_name = get_trigger_name(name, trigger)

    @router.get(path=view_name, name=view_name)
    async def _view(user_input: str):
        trigger_func = get_trigger(name, trigger)

        if trigger_func:
            trigger_func(user_input)

        template = get_template("{}.html".format(name))

        if name == "xss" and trigger == "raw":
            template += "<p>XSS: " + user_input + "</p>"

        return HTMLResponse(template)


def generate_root_urls():
    for name in TRIGGER_MAP:
        gen_root_view(name)
