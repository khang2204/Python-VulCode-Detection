cache[args] = func(*args)
        return cache[args]

    return wrapper


@cache
def get_template(path):
    """
    Read and return the contents of the file at TEMPLATES_LOCATON/<path>.
    This is vulnerable to path traversal if used incorrectly, but security clearly
    isn't a concern if you're using `vulnpy`.
    """
    filename = os.path.join(TEMPLATES_LOCATION, path)
    with open(filename, "r") as f:
        return f.read()
