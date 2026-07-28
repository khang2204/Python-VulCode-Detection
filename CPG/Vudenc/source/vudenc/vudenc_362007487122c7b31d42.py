def inRange(self, node1, node2):...
xDistance = node1['x'] - node2['x']
yDistance = node1['y'] - node2['x']
distance = math.sqrt(xDistance * xDistance + yDistance * yDistance)
return distance <= self.commRange
