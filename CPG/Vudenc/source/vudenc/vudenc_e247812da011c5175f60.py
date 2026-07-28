def trunc(string, length=128):...
"""docstring"""
if string is None:
return ''
string = string[:length] + ' ...' if len(string) > length else string
return string
