def testSquare(self, length, corners):...
"""docstring"""
if not self.reached_corner[self.corner_counter]:
self.reached_corner[self.corner_counter] = self.navloc.goToPosition(corners
    [self.corner_counter][0] * length, corners[self.corner_counter][1] * length
    )
self.logArrival('corner ' + str(self.corner_counter), corners[self.
    corner_counter][0] * length, corners[self.corner_counter][1] * length)
if self.corner_counter == len(self.reached_corner) - 1:
self.reached_corner = [False] * len(self.reached_corner)
self.corner_counter = (self.corner_counter + 1) % len(self.reached_corner)
