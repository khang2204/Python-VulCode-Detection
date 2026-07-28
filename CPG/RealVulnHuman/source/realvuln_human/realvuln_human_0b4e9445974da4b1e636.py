pattern = re.compile(PATTERN)
    for match in pattern.finditer(user_input):
        match.group(0)


def do_re_findall(user_input):
    return re.findall(PATTERN, user_input)


def do_re_findall_compiled(user_input):
    pattern = re.compile(PATTERN)
    return pattern.findall(user_input)


def do_re_fullmatch(user_input):
    match = re.fullmatch(PATTERN, user_input)
    if match:
        return match.group(0)


def do_re_fullmatch_compiled(user_input):
    pattern = re.compile(PATTERN)
