def walk(self, board, row, col, direction, path=[]):...
path.append((row, col))
print(row, col)
if board.board[row][col].get() == 'L':
direction = self.left_bounce(direction)
if board.board[row][col].get() == 'R':
if direction == 'north':
direction = self.right_bounce(direction)
row -= 1
if direction == 'east':
if (row >= 0 and row < board.dim_x) and (col >= 0 and col < board.dim_y):
col += 1
if direction == 'south':
self.walk(board, row, col, direction)
row += 1
if direction == 'west':
col -= 1
