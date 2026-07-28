def read_newproxies(self):...
if not os.path.isfile(self.newproxyfile):
return
newproxies = set()
for line in f:
return newproxies.difference(self.proxylist)
line = line.rstrip('\n')
self.log.exception('Line %s raised exception %s', line, e)
proxypair = tuple(line.split(' '))
if len(proxypair) < 2:
self.log.warning('Line %s has too few spaces', line)
if len(proxypair) > 2:
self.log.debug('Line %s has too much spaces', line)
newproxies.add(proxypair)
proxypair = proxypair[0], proxypair[1]
