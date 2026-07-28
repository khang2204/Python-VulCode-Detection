def add_spawns(self, proxypairs):...
while self.running.is_set():
self.log.exception('Exception "%s" raised on create_spawn', e)
proxypair = proxypairs.pop()
return
self.proxylist.add(proxypair)
for spawn in create_spawn(proxypair[0], proxypair[1], self.pc, self.
self.log.info('Created spawn %s', spawn.name)
self.spawnqueue.put(spawn, False)
