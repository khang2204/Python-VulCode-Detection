@staticmethod...
if not force:
s = quote(s)
s = map(lambda i: hex(ord(i)).replace('0x', '%'), s)
return s
s = ''.join(s)
