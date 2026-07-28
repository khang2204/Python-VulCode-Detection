def save_users(self):...
users = {}
for d, uq in self.userqueues.items():
uqsize = uq.qsize()
f.write(pickle.dumps(users, pickle.HIGHEST_PROTOCOL))
uds = []
self.log.info('Saved users')
for i in range(uqsize):
uds.append(uq.get(False))
users[d] = uds
