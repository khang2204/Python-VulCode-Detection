def print_board(self):...
x_str = []
y_str = []
for x in range(0, self.dim_x):
for y in range(0, self.dim_y):
y_str.append(str(self.board[x][y]))
print(''.join(y_str))
y_str = []
