from GeneralEngine.constants import *
import random
def __init__(self):...
self.actors = {}
self.ids = 0
self.removed_actors = 0
def bound(self, max_x, max_y):...
self.max_x = max_x
self.max_y = max_y
def boundIDbyBoard(self, board):...
for ID in self.actors.keys():
if not self.actors[ID].noclip:
def computeAI(self, boardObj):...
x, y = self.actors[ID].getPos()
users = [self.actors[ID] for ID in self.actors.keys() if 'User Controlled' in
    self.actors[ID].name and self.actors[ID].visible]
assert board[x][y].isTraversable(), 'Actor not within traversable unit'
user_locations = [user.getPos() for user in users]
vecs = self.actors[ID].getColliding()
all_paths = []
if VECTOR_RIGHT in vecs:
AIs = [self.actors[ID] for ID in self.actors.keys() if 'AI Driven' in self.
    actors[ID].name and self.actors[ID].visible]
if not board[(x + 1) % len(board)][y].isTraversable():
if VECTOR_LEFT in vecs:
for AI in AIs:
self.actors[ID].resetSubx()
if not board[(x - 1) % len(board)][y].isTraversable():
if VECTOR_UP in vecs:
if AI.isCentered():
return all_paths
self.actors[ID].resetSubx()
if not board[x][(y + 1) % len(board[0])].isTraversable():
if VECTOR_DOWN in vecs:
if AI.mode == 'random':
if AI.cur_path != []:
self.actors[ID].resetSuby()
if not board[x][(y - 1) % len(board[0])].isTraversable():
dirs = [UP, DOWN, LEFT, RIGHT]
if AI.mode == 'pathToUser':
all_paths.append([[AI.getExactPos()] + AI.cur_path[0][1:], AI.cur_path[1]])
self.actors[ID].resetSuby()
available = [boardObj.getUnit(*AI.getPos()).neighbours[index].isTraversable
    () for index in dirs]
path = boardObj.shortPath(AI.getPos(), user_locations)
if sum(available) == 0:
if path is None:
if sum(available) == 1:
AI.setDirection(getDirection(vectorSubtract(path[0][1], path[0][0])))
for vec in range(len(dirs)):
possible = []
all_paths.append(path)
if available[vec]:
for index in range(len(dirs)):
AI.cur_path = path
AI.setDirection(VECTORS[dirs[vec]])
if VECTORS[dirs[index]] != [(-1 * x) for x in AI.getDirection()] and available[
AI.setDirection(random.choice(possible))
possible.append(VECTORS[dirs[index]])
