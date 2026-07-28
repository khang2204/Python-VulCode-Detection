def _seed(user_input):
    """
    For seeding to be deterministic in PY2 we need to pass in an integer
    """
    random.seed(user_input)


def do_random(user_input):
    _seed(user_input)
    return str(random.random())


def do_randint(user_input):
    _seed(user_input)
    return str(random.randint(0, 100))


def do_randrange(user_input):
    _seed(user_input)
    return str(random.randrange(0, 101, 5))
