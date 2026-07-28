h = hashlib.md5()
    return _hash(h, user_input)


def do_hashlib_sha1(user_input):
    h = hashlib.sha1()
    return _hash(h, user_input)


def do_hashlib_new(user_input):
    h = hashlib.new("SHA1")
    return _hash(h, user_input)
