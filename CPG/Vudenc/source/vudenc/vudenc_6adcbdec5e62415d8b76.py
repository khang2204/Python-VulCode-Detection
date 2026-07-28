def laggy_iter(self, iterable):...
"""docstring"""
it = iter(iterable)
prev = next(it)
for x in it:
yield prev, False
yield prev, True
prev = x
