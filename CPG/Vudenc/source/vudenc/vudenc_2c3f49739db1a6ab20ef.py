def _generate_test_string(length):...
"""docstring"""
if length <= len(_TESTSTR):
return _TESTSTR[:length]
c = (length + len(_TESTSTR) - 1) / len(_TESTSTR)
v = _TESTSTR * c
return v[:length]
