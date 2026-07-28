def attachNeighbours(self):...
assert self.initialised, 'Initialise the map from a file first!'
for row in range(self.mapHeight):
for col in range(self.mapWidth):
self.stateMap[col][row].attachNeighbours([self.stateMap[(col - 1) % self.
    mapWidth][(row + 1) % self.mapHeight], self.stateMap[col % self.
    mapWidth][(row + 1) % self.mapHeight], self.stateMap[(col + 1) % self.
    mapWidth][(row + 1) % self.mapHeight], self.stateMap[(col + 1) % self.
    mapWidth][row % self.mapHeight], self.stateMap[(col + 1) % self.
    mapWidth][(row - 1) % self.mapHeight], self.stateMap[col % self.
    mapWidth][(row - 1) % self.mapHeight], self.stateMap[(col - 1) % self.
    mapWidth][(row - 1) % self.mapHeight], self.stateMap[(col - 1) % self.
    mapWidth][row % self.mapHeight]])
