def do_re_match_compiled(user_input):
    pattern = re.compile(PATTERN)
    match = pattern.match(user_input)
    if match:
        return match.group(0)


def do_re_search(user_input):
    match = re.search(PATTERN, user_input)
    if match:
        return match.group(0)


def do_re_search_compiled(user_input):
    pattern = re.compile(PATTERN)
    match = pattern.search(user_input)
    if match:
        return match.group(0)
