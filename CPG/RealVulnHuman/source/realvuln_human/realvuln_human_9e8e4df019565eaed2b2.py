import pickle
import yaml


def do_pickle_load(user_input):
    user_input = io.BytesIO(user_input.encode("utf-8"))
    return pickle.load(user_input)


def do_pickle_loads(user_input):
    return pickle.loads(user_input.encode("utf-8"))


def do_yaml_load(user_input):
    try:
        return yaml.load(user_input, Loader=yaml.UnsafeLoader)
    except yaml.constructor.ConstructorError:
        pass


def do_yaml_load_all(user_input):
