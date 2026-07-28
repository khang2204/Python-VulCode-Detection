def csvLogMap(self, test_name, folder='tests'):...
"""docstring"""
self._logger.csv(test_name + '_mappose', ['X', 'Y', 'yaw'], [self.map_pos.x,
    self.map_pos.y, self.map_angle], folder=folder)
