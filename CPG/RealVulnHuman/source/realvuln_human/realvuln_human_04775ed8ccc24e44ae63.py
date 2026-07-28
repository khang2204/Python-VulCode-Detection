or len(path_components) > 3
        or path_components[0] != "vulnpy"
    ):
        raise NotFound()
    if len(path_components) == 1:
        return "home", None

    name = path_components[1]
    if name not in TRIGGER_MAP:
        raise NotFound()
    # we need to do this to avoid path traversal during template resolution
    sanitized_name = [s for s in TRIGGER_MAP.keys() if s == name][0]

    if len(path_components) == 2:
        return sanitized_name, None

    return sanitized_name, _get_trigger_func(sanitized_name, path_components[2])


def _get_trigger_func(name, trigger_name):
    """
    Given a valid vulnerability name, get the trigger function corresponding
