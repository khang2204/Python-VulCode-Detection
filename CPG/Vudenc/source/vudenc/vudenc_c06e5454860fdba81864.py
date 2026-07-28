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
lkvm = lkvm + 1
