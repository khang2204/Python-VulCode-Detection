def addNewNode(self, index):...
x = random.randint(0, self.width)
y = random.randint(0, self.width)
keys = set()
while len(keys) < self.keysPerNode:
keys.add(random.randint(0, self.keyPoolSize))
self.G.add_node(index, x=x, y=y, keys=keys)
