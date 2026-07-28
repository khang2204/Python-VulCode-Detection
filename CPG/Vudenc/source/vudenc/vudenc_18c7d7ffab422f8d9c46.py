def _ekfCallback(self, data):...
"""docstring"""
Navigation._ekfCallback(self, data)
self.map_pos = self.transformPoint(self.p, 'odom', 'map')
self.map_angle = self.transformAngle(self.angle, 'odom', 'map')
