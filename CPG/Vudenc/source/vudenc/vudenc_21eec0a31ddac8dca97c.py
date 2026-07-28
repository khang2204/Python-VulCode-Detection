def __init__(self):...
Tester.__init__(self, 'NavLoc')
self.jerky = False
self.walking_speed = 1
self.reached_goal = False
self.reached_corner = [False, False, False, False]
self.cc_square = [(0, 0), (1, 0), (1, 1), (0, 1)]
self.c_square = [(0, 0), (1, 0), (1, -1), (0, -1)]
self.corner_counter = 0
self.test_name = 'path'
point_ids = MD2.points
locations = MD2.locations
neighbors = MD2.neighbors
landmarks = MD2.landmarks
landmark_positions = MD2.landmark_pos
landmark_orientations = MD2.landmark_orient
self.navloc = NavLoc(point_ids, locations, neighbors, landmarks,
    landmark_positions, landmark_orientations, jerky=self.jerky,
    walking_speed=self.walking_speed)
self.destination = [self.navloc.floorplan.graph['T'].location, self.navloc.
    floorplan.graph['R'].location]
