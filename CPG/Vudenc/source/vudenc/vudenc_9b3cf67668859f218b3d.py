def _init_board(self):...
for x in range(0, self.dim_x):
self.board.append([])
for y in range(0, self.dim_y):
empty_grid = Grid()
self.board[x].append(empty_grid)
