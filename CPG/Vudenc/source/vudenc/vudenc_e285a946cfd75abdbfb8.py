def remote_listing(self, host, path):...
logging.debug('API: Getting remote host %s path %s contents' % (host, path))
contents = list()
logging.debug('Checking path %s' % path)
if not self.remote_exists(host, path):
while not self.remote_exists(host, path):
for line in self.remote_iterdir(host, path):
logging.debug('Path does not exist, working up the tree...')
logging.debug(line)
return contents
logging.debug(path.as_posix())
if len(line) > 0 and line != './' and line != '../':
path = path.parent
if line[-1] == '/':
contents.append({'type': 'dir', 'name': line[:-1]})
if line[-1] == '@':
contents.append({'type': 'link', 'name': line[:-1]})
if line[-1] == '*':
contents.append({'type': 'file', 'name': line[:-1]})
if line[-1] not in ['#']:
contents.append({'type': 'file', 'name': line})
