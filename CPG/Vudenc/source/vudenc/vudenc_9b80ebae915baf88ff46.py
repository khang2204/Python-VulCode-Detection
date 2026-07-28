def calc_board_count(self, board_str):...
board_split = board_str.split(':')[1].split(',')
board_count_start = 4
top_row = board_split[board_count_start:board_count_start + self.dim_x]
right_col = board_split[board_count_start + self.dim_x:board_count_start +
    self.dim_x + self.dim_y]
bottom_row = board_split[board_count_start + self.dim_x + self.dim_y:
    board_count_start + self.dim_x * 2 + self.dim_y]
left_col = board_split[board_count_start + self.dim_x * 2 + self.dim_y:
    board_count_start + self.dim_x * 2 + self.dim_y * 2]
return top_row, right_col, bottom_row, left_col
