def __init__(self, dump=None):...
self.dumpfilepath = ''
if dump:
self.dumpfilepath = 'kijiji_dump_{}.txt'.format(strftime('%Y%m%dT%H%M%S'))
f.write(dump)
