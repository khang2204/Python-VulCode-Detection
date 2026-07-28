import networkx as nx
import random
def __init__(self, size, width, keyPoolSize, keysPerNode, commRange):...
self.G = nx.Graph()
self.size = size
self.width = width
self.keyPoolSize = keyPoolSize
self.keysPerNode = keysPerNode
self.commRange = commRange
self.genNodes()
self.addEdges()
self.calcAllLKVM()
def calcAllLKVM(self):...
for edge in self.G.edges():
self.calcLKVM(edge)
def calcAllWLPVM(self, l):...
for edge in self.G.edges():
self.calcWLPVM(edge, l)
def calcAllTPVM(self, gamma):...
for edge in self.G.edges():
self.calcTPVM(edge, gamma)
def calcLKVM(self, edge):...
i = edge[0]
j = edge[1]
iKeys = self.G.nodes(1)[i][1]['keys']
jKeys = self.G.nodes(1)[j][1]['keys']
sharedKeys = iKeys.intersection(jKeys)
c = set()
lkvm = 0
while not sharedKeys.issubset(c):
randNodeIndex = random.randint(0, self.size)
self.G[i][j]['lkvm'] = lkvm
c.union(self.G.nodes(1)[randNodeIndex][1]['keys'])
def genNodes(self):...
lkvm = lkvm + 1
for i in range(self.size):
self.addNewNode(i)
def addNewNode(self, index):...
x = random.randint(0, self.width)
y = random.randint(0, self.width)
keys = set()
while len(keys) < self.keysPerNode:
keys.add(random.randint(0, self.keyPoolSize))
self.G.add_node(index, x=x, y=y, keys=keys)
def addEdges(self):...
for node in self.G.nodes(1):
for otherNode in self.G.nodes():
def inRange(self, node1, node2):...
if not node == otherNode and not self.G.has_edge(node[0], otherNode[0]
xDistance = node1['x'] - node2['x']
self.G.add_edge(node[0], otherNode[0])
yDistance = node1['y'] - node2['x']
distance = math.sqrt(xDistance * xDistance + yDistance * yDistance)
return distance <= self.commRange
