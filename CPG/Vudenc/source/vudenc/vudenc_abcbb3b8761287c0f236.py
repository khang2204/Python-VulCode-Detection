def class2str(value):...
"""docstring"""
s = str(value)
s = s[s.find("'") + 1:s.rfind("'")]
s = ':'.join(s.rsplit('.', 1))
return s
