return str(random.randint(0, 100))


def do_randrange(user_input):
    _seed(user_input)
    return str(random.randrange(0, 101, 5))


def do_uniform(user_input):
    _seed(user_input)
    return str(random.uniform(5.5, 7.5))
