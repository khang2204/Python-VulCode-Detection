def do_tarfile_bz2(user_input):
    try:
        with tarfile.open(user_input, mode="r:bz2") as tf:
            return tf.getmembers()[0].name
    except Exception:
        return None


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
