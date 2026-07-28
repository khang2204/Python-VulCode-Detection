@staticmethod...
board_split = board_str.split(':')[1].split(',')
ghost_count = int(board_split[0])
vampire_count = int(board_split[1])
zombie_count = int(board_split[2])
return ghost_count, vampire_count, zombie_count
