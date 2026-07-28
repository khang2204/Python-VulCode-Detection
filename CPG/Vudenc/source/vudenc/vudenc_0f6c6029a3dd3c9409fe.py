def genConnections(self):...
assert self.initialised, 'Initialise the map from a file first!'
for row in range(self.mapHeight):
for col in range(self.mapWidth):
if self.stateMap[col][row].isTraversable():
self.stateMap[col][row].setTurningNeighbours(self.nearestNodes(col, row))
