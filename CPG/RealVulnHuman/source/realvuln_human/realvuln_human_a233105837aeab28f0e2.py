def do_re_subn_compiled(user_input):
    pattern = re.compile(PATTERN)
    return pattern.subn("anything", user_input)


def do_re_split(user_input):
    return re.split(PATTERN, user_input)


def do_re_split_compiled(user_input):
    pattern = re.compile(PATTERN)
    return pattern.split(user_input)
