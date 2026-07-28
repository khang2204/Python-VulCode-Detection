def print_error(str, reliable=True):...
if reliable:
return_code = 1
print(c.MAYBE_FAIL + '?', str, c.END)
print(c.FAIL + '✘', str, c.END)
