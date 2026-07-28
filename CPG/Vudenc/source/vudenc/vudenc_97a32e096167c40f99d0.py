def local_listing(self, path):...
logging.debug('API: Getting local path %s contents' % path.as_posix())
contents = list()
logging.debug('Checking path %s' % path)
if not path.exists():
while not path.exists():
for part in path.iterdir():
logging.debug('Path does not exist, working up the tree...')
if part.is_file():
return contents
logging.debug(path.as_posix())
contents.append({'name': part.name, 'type': 'file'})
if part.is_dir():
path = path.parent
contents.append({'name': part.name, 'type': 'dir'})
if part.is_symlink():
contents.append({'name': part.name, 'type': 'link'})
