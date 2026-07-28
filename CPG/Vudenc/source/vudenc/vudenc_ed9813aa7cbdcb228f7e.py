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
