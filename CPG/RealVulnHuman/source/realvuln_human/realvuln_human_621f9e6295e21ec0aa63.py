try:
        with open(user_input) as f:
            return f.read()
    except Exception:
        return None


def do_execfile(user_input):
    """only exists in PY2"""
    try:
        execfile(user_input)  # noqa: F821
    except Exception:
        pass
