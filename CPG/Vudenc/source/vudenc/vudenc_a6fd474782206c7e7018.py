def dump_database(self, sqlfile):...
"""docstring"""
if self.connection:
for line in self.connection.iterdump():
f.write('%s\n' % line)
print('db dumped to %s' % sqlfile[0])
