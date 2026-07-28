def generate_board(self, board_str):...
board_split = board_str.split(':')[1].split(',')
board_layout = board_split[3]
x = 0
y = 0
for space in board_layout:
if space == 'L' or space == 'R':
self.board[x][y].set(space)
for count in range(0, ord(space) - 96):
if y < self.dim_y - 1:
self.board[x][y].set(' ')
y += 1
y = 0
if y < self.dim_y - 1:
x += 1
y += 1
y = 0
x += 1
