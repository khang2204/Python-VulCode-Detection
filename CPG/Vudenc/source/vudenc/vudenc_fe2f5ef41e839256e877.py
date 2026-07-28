def addEdges(self):...
for node in self.G.nodes(1):
for otherNode in self.G.nodes():
if not node == otherNode and not self.G.has_edge(node[0], otherNode[0]
self.G.add_edge(node[0], otherNode[0])
