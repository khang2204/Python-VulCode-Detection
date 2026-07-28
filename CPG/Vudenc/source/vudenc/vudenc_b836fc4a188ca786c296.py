@staticmethod...
"""docstring"""
dims = []
for dim in board_str.split(':')[0].split('x'):
dims.append(int(dim))
return dims[0], dims[1]
