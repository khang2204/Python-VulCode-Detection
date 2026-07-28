def __init__(self, board_str):...
self.dim_x, self.dim_y = self.calc_dim(board_str)
self.g_count, self.v_count, self.z_count = self.calc_monster_count(board_str)
self.board = []
self._init_board()
self.generate_board(board_str)
self.north_count, self.east_count, self.south_count, self.west_count = (self
    .calc_board_count(board_str))
