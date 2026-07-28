def getCollisionCommands(self):...
all_commands = []
keys = list(self.actors.keys())
for ind1 in range(len(keys)):
for ind2 in range(ind1 + 1, len(keys)):
return all_commands
commands = self.actors[keys[ind1]].collideWith(self.actors[keys[ind2]])
all_commands = all_commands + commands
