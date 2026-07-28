def cache(self, limit):...
"""docstring"""
log.debug('Start caching last active users from the DB...')
last_active_users = self.get_last_active_users(limit)
log.error('Cannot cache users!')
for items in last_active_users:
return
if items[0] not in self.users:
log.info('Users have been cached.')
self.users[items[0]] = User(*items)
log.debug('Caching user: %s', self.users[items[0]])
