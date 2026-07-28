def csvLogArrival(self, test_name, x, y, folder='tests'):...
"""docstring"""
self._logger.csv(test_name + '_waypoints', ['X_target', 'Y_target', 'X_map',
    'Y_map', 'X_ekf', 'Y_ekf'], [x, y, self.map_pos.x, self.map_pos.y, self
    .p.x, self.p.y], folder=folder)
