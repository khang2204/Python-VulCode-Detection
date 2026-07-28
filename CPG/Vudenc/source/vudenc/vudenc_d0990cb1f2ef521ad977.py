def logArrival(self, name, x, y):...
self.logger.info('Arrived at ' + str((x, y)) + ' (map position is ' + str((
    self.navloc.map_pos.x, self.navloc.map_pos.y)) + ')')
self.navloc.csvLogArrival(self.test_name, x, y)
