def do_yaml_load(user_input):
    try:
        return yaml.load(user_input, Loader=yaml.UnsafeLoader)
    except yaml.constructor.ConstructorError:
        pass


def do_yaml_load_all(user_input):
    result = yaml.load_all(user_input, Loader=yaml.UnsafeLoader)
    # load_all returns a generator so we need to force the load to be evaluated
    try:
        return list(result)
    except yaml.constructor.ConstructorError:
        pass
