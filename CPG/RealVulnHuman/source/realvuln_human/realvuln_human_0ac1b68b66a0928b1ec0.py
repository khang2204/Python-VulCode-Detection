import io
import tarfile
import bz2


def do_tarfile_open(user_input):
    try:
        with tarfile.TarFile.open(user_input, mode="r:") as tf:
            return tf.getmembers()[0].name
    except Exception:
        return None


def do_tarfile_class(user_input):
    try:
        with tarfile.TarFile(user_input) as tf:
            return tf.getmembers()[0].name
    except Exception:
