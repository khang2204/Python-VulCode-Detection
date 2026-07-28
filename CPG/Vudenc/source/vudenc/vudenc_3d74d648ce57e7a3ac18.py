def _handleObstacle(self, turn_delta):...
"""docstring"""
if Navigation._handleObstacle(self, turn_delta):
self._path = None
return False
return True
