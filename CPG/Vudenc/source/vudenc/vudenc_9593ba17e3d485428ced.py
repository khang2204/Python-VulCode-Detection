def testLine(self, length):...
"""docstring"""
if self.test_name is None:
self.initFile('line')
if not self.reached_corner[0]:
self.reached_corner[0] = self.navloc.goToPosition(0, 0)
if self.navloc.goToPosition(length, 0):
if self.reached_corner[0]:
self.reached_corner[0] = False
self.logArrival('home', 0, 0)
self.logArrival('endpoint', length, 0)
