def moveActor(self, ID, x, y):...
assert 0 <= x <= self.max_x, 'X-axis incorrect value {}'.format(x)
assert 0 <= y <= self.max_y, 'Y-axis incorrect value {}'.format(y)
self.actors[ID].x = x
self.actors[ID].y = y
self.actors[ID].resetSubx()
self.actors[ID].resetSuby()
