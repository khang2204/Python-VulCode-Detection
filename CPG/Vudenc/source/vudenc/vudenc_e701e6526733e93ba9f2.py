def testPath(self):...
"""docstring"""
if not self.reached_corner[0]:
self.reached_corner[0] = self.navloc.takePathToDest(self.destination[0].x,
    self.destination[0].y)
if self.navloc.takePathToDest(self.destination[1].x, self.destination[1].y):
if self.reached_corner[0]:
self.reached_corner[0] = False
self.logArrival('office 1', self.destination[0].x, self.destination[0].y)
self.logArrival('office 2', self.destination[1].x, self.destination[1].y)
