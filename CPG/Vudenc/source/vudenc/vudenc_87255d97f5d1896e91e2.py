def takePathToDest(self, x, y):...
"""docstring"""
if self._path is None:
self._path = self.floorplan.getShortestPath(self.map_pos, Point(x, y, 0))
if self.goToPosition(self._path[0].x, self._path[0].y):
self._logger.info('Arrived at waypoint ' + str((self._path[0].x, self._path
    [0].y)) + ' (map position is ' + str((self.map_pos.x, self.map_pos.y)) +
    ')')
if not self._path:
self._path.pop(0)
self._path = None
return False
self._logger.debug('no path!')
return True
