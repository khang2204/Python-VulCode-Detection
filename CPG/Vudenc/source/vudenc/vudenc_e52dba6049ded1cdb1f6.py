def getNodeConnectionCoords(self):...
coords = []
for x, y in self.turningNodes:
z = 0
return coords
for turn in self.stateMap[x][y].getTurning():
if turn != -1:
coords.append([(x, y), turn[0], turn[1]])
z += 1
