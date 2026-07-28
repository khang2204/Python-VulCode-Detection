def breaks(string):...
"""docstring"""
if string is None:
return string
for n in breaks_list:
string = string.replace(n, n + '<wbr>')
return string
