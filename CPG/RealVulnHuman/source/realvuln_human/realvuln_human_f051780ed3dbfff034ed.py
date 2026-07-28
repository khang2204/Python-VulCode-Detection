def do_re_sub(user_input):
    return re.sub(PATTERN, "anything", user_input)


def do_re_sub_compiled(user_input):
    pattern = re.compile(PATTERN)
    return pattern.sub("anything", user_input)


def do_re_subn(user_input):
    return re.subn(PATTERN, "anything", user_input)


def do_re_subn_compiled(user_input):
    pattern = re.compile(PATTERN)
    return pattern.subn("anything", user_input)


def do_re_split(user_input):
    return re.split(PATTERN, user_input)
