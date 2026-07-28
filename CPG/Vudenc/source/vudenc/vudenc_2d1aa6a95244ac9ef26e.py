from GeneralEngine.Unit import *
import numpy as np
from GeneralEngine.BinaryHeap import BinaryHeap, Node
def __init__(self):...
self.initialised = False
self.board = None
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
def resetToOriginal(self):...
self.attachNeighbours()
self.identifyTurning()
self.genConnections()
def attachNeighbours(self):...
assert self.initialised, 'Initialise the map from a file first!'
for row in range(self.mapHeight):
for col in range(self.mapWidth):
def identifyTurning(self):...
self.stateMap[col][row].attachNeighbours([self.stateMap[(col - 1) % self.
    mapWidth][(row + 1) % self.mapHeight], self.stateMap[col % self.
    mapWidth][(row + 1) % self.mapHeight], self.stateMap[(col + 1) % self.
    mapWidth][(row + 1) % self.mapHeight], self.stateMap[(col + 1) % self.
    mapWidth][row % self.mapHeight], self.stateMap[(col + 1) % self.
    mapWidth][(row - 1) % self.mapHeight], self.stateMap[col % self.
    mapWidth][(row - 1) % self.mapHeight], self.stateMap[(col - 1) % self.
    mapWidth][(row - 1) % self.mapHeight], self.stateMap[(col - 1) % self.
    mapWidth][row % self.mapHeight]])
assert self.initialised, 'Initialise the map from a file first!'
self.turningNodes = []
for row in range(self.mapHeight):
for col in range(self.mapWidth):
def genConnections(self):...
if self.stateMap[col][row].isTraversable():
assert self.initialised, 'Initialise the map from a file first!'
self.stateMap[col][row].identifyTurning()
for row in range(self.mapHeight):
if self.stateMap[col][row].isTurning():
for col in range(self.mapWidth):
def nearestNodes(self, x, y):...
self.turningNodes.append([col, row])
if self.stateMap[col][row].isTraversable():
assert self.turningNodes != [], 'Empty turning nodes!'
self.stateMap[col][row].setTurningNeighbours(self.nearestNodes(col, row))
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
