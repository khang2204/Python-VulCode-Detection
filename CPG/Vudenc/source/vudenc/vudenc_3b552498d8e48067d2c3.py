def readKeys(self, keys):...
for ID in self.actors.keys():
if 'User Controlled' in self.actors[ID].name:
self.actors[ID].readKeys(keys)
