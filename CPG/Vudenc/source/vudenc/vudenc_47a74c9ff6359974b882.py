def __init__(self, min_repeat=50, max_repeat=100):...
"""docstring"""
self.regex = re.compile(
    '((?P<value>.+)(?P=value){{{min_repeat},{max_repeat}}})$'.format(
    min_repeat=min_repeat - 1, max_repeat=max_repeat - 1))
