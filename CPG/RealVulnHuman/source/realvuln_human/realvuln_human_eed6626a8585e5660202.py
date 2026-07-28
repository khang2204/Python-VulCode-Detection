def _view():
    user_input = _get_user_input()
    trigger_func = get_trigger(name, trigger)

    if trigger_func:
        trigger_func(user_input)

    template = get_template("{}.html".format(name))

    if name == "xss" and trigger == "raw":
        template += "<p>XSS: " + user_input + "</p>"

    return template

view_name = get_trigger_name(name, trigger)

vulnerable_blueprint.add_url_rule(
    view_name, view_name, _view, methods=["GET", "POST"], strict_slashes=False
)
return _view
