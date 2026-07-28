def do_bz2_class(user_input, size=0):
    try:
        with bz2.BZ2File(user_input) as bz2file:
            return bz2file.read(size)
    except Exception:
        return None


def do_bz2_open(user_input, size=0):
    try:
        with bz2.open(user_input) as bz2file:
            return bz2file.read(size)
    except Exception:
        return None


def do_io_open(user_input):
    try:
        with io.open(user_input) as f:
            return f.read()
    except Exception:
