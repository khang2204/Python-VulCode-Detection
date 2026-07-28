def computeAI(self, boardObj):...
users = [self.actors[ID] for ID in self.actors.keys() if 'User Controlled' in
    self.actors[ID].name and self.actors[ID].visible]
user_locations = [user.getPos() for user in users]
all_paths = []
AIs = [self.actors[ID] for ID in self.actors.keys() if 'AI Driven' in self.
    actors[ID].name and self.actors[ID].visible]
for AI in AIs:
if AI.isCentered():
return all_paths
if AI.mode == 'random':
if AI.cur_path != []:
dirs = [UP, DOWN, LEFT, RIGHT]
if AI.mode == 'pathToUser':
all_paths.append([[AI.getExactPos()] + AI.cur_path[0][1:], AI.cur_path[1]])
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
