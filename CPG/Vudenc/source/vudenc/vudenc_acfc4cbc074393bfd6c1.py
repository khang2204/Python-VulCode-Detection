def force_bytes(s):...
if isinstance(s, bytes):
return s
return s.encode('utf-8', 'replace')
