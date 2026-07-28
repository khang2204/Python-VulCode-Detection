@staticmethod...
name = '%s.cfg' % hostname
if name != os.path.basename(name):
msg = 'Directory traversal attempt detected for host name %r'
return name
