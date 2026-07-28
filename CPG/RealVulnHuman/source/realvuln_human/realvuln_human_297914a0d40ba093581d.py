return pattern.findall(user_input)


def do_re_fullmatch(user_input):
    match = re.fullmatch(PATTERN, user_input)
    if match:
        return match.group(0)


def do_re_fullmatch_compiled(user_input):
    pattern = re.compile(PATTERN)
    match = pattern.fullmatch(user_input)
    if match:
        return match.group(0)


def do_re_sub(user_input):
    return re.sub(PATTERN, "anything", user_input)


def do_re_sub_compiled(user_input):
    pattern = re.compile(PATTERN)
