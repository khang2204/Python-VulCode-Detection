def identifyTurning(self):...
assert self.initialised, 'Initialise the map from a file first!'
self.turningNodes = []
for row in range(self.mapHeight):
for col in range(self.mapWidth):
if self.stateMap[col][row].isTraversable():
self.stateMap[col][row].identifyTurning()
if self.stateMap[col][row].isTurning():
self.turningNodes.append([col, row])
