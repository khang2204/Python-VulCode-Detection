def goToOrientation(self, angle):...
"""docstring"""
return Navigation.goToOrientation(self, self.transformAngle(angle, 'map',
    'odom'))
