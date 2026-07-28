def do_re_search_compiled(user_input):
    pattern = re.compile(PATTERN)
    match = pattern.search(user_input)
    if match:
        return match.group(0)


def do_re_finditer(user_input):
    for match in re.finditer(PATTERN, user_input):
        match.group(0)


def do_re_finditer_compiled(user_input):
    pattern = re.compile(PATTERN)
    for match in pattern.finditer(user_input):
        match.group(0)


def do_re_findall(user_input):
