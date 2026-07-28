def boundIDbyBoard(self, board):...
for ID in self.actors.keys():
if not self.actors[ID].noclip:
x, y = self.actors[ID].getPos()
assert board[x][y].isTraversable(), 'Actor not within traversable unit'
vecs = self.actors[ID].getColliding()
if VECTOR_RIGHT in vecs:
if not board[(x + 1) % len(board)][y].isTraversable():
if VECTOR_LEFT in vecs:
self.actors[ID].resetSubx()
if not board[(x - 1) % len(board)][y].isTraversable():
if VECTOR_UP in vecs:
self.actors[ID].resetSubx()
if not board[x][(y + 1) % len(board[0])].isTraversable():
if VECTOR_DOWN in vecs:
self.actors[ID].resetSuby()
if not board[x][(y - 1) % len(board[0])].isTraversable():
self.actors[ID].resetSuby()
