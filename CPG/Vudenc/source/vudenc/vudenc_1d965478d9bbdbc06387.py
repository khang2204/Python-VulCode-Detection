def load_users(self):...
if not os.path.isfile(self.usersfile):
return
users = pickle.loads(f.read())
for domain in users.keys():
self.log.exception(e)
uq = Queue()
self.log.error('Failed to load users')
for ud in users[domain]:
self.log.debug('Loaded user %s:%s', domain, ud['login'])
self.userqueues[domain] = uq
uq.put(ud)
