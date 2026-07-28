def goToPosition(self, x, y):...
"""docstring"""
transformed_point = self.transformPoint(Point(x, y, 0), 'map', 'odom')
return Navigation.goToPosition(self, transformed_point.x, transformed_point.y)
