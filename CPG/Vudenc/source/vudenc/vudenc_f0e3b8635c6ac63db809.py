def nearestNodes(self, x, y):...
assert self.turningNodes != [], 'Empty turning nodes!'
found = [0, 0, 0, 0]
current = [[(x - 1) % self.mapWidth, y % self.mapHeight], [x % self.
    mapWidth, (y + 1) % self.mapHeight], [(x + 1) % self.mapWidth, y % self
    .mapHeight], [x % self.mapWidth, (y - 1) % self.mapHeight]]
while 0 in found:
for z in range(len(current)):
return found
if found[z] == 0:
if self.stateMap[current[z][0]][current[z][1]].isTraversable():
if found[z] == 0:
if current[z][0] == x and current[z][1] == y:
found[z] = -1
if z % 2 == 0:
found[z] = [current[z], 'y' if z % 2 else 'x']
if self.stateMap[current[z][0]][current[z][1]].isTurning():
current[z][0] = (current[z][0] + z - 1) % self.mapWidth
current[z][1] = (current[z][1] + 2 - z) % self.mapHeight
if z == 0:
found[z] = [current[z], 'x' if current[z][0] > x else None]
if z == 1:
found[z] = [current[z], 'y' if current[z][1] < y else None]
if z == 2:
found[z] = [current[z], 'x' if current[z][0] < x else None]
if z == 3:
found[z] = [current[z], 'y' if current[z][1] > y else None]
