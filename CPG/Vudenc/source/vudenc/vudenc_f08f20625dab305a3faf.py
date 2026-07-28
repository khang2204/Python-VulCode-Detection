def grouper(iterable, n, fillvalue=None):...
"""docstring"""
args = [iter(iterable)] * n
return izip_longest(*args, fillvalue=fillvalue)
