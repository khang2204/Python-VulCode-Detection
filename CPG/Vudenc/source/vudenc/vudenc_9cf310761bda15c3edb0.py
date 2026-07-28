def initialiseMapFromFile(self, filename):...
file = open(filename, 'r')
self.mapType = file.readline().split(' ')[1]
self.mapHeight = int(file.readline().split(' ')[1])
self.mapWidth = int(file.readline().split(' ')[1])
assert file.readline().rstrip('\n') == 'map', 'Unknown map format'
self.originalMap = [['def' for col in range(self.mapHeight)] for row in
    range(self.mapWidth)]
for row in range(self.mapHeight):
tRow = file.readline().rstrip('\n')
self.initialised = True
for col in range(self.mapWidth):
self.resetToOriginal()
self.originalMap[col][self.mapHeight - row - 1] = tRow[col]
