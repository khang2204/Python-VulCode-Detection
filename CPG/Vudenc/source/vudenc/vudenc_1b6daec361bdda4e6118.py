def __init__(self, point_ids, locations, neighbors, landmark_ids,...
self.map_pos = Point()
self.map_angle = 0
self._path = None
Localization.__init__(self, point_ids, locations, neighbors, landmark_ids,
    landmark_positions, landmark_angles)
Navigation.__init__(self, jerky=jerky, walking_speed=walking_speed)
self._logger = Logger('NavLoc')
timer = time()
while time() - timer < 0.5:
