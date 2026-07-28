def _fmt_msg(self, msg):...
width = 80
_fmt = ''
for line in msg.splitlines():
_fmt = _fmt + fill(line, width, replace_whitespace=False) + '\n'
return _fmt
