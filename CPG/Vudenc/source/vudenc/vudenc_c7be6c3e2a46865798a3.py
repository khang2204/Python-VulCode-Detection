def shortPath(self, start_coord, end_coords):...
paths = []
start_x, start_y = start_coord
for end in end_coords:
end_x, end_y = end
if paths == []:
found = False
return None
cur_min = paths[0]
if end_x == start_x and end_y == start_y:
for x in range(1, len(paths)):
return None
end_neighbour = self.stateMap[end_x][end_y].getTurning()
if cur_min[1] > paths[x][1]:
return cur_min
start_neighbour = self.stateMap[start_x][start_y].getTurning()
cur_min = paths[x]
for index in range(len(end_neighbour)):
if end_neighbour[index] != -1 and start_neighbour[index
if not found:
found = True
end_points = [(neigh[0], self.getDist((end_x, end_y), neigh[0])) for neigh in
    end_neighbour if neigh != -1]
paths.append([[[start_x, start_y], [end_x, end_y]], self.getDist((start_x,
    start_y), (end_x, end_y))])
heap = BinaryHeap()
nid = self.coordToID(start_x, start_y)
g_ = 0
f_ = self.getDist((start_x, start_y), (end_x, end_y))
heap.pool[nid] = Node(nid, g_, f_, None)
heap.insert(nid)
while not found and heap.size >= 0:
removed = heap.remove()
cur_x, cur_y = self.IDToCoord(removed)
for endTurn in end_points:
if endTurn[0][0] == cur_x and endTurn[0][1] == cur_y and not found:
if not found:
cur_path = [(end_x, end_y), endTurn[0]]
newTurning = self.stateMap[cur_x][cur_y].getTurning()
cur_elem = heap.pool[removed]
for node in newTurning:
dist = endTurn[1]
if node != -1:
while cur_elem.prevID != None:
nid = self.coordToID(node[0][0], node[0][1])
coord1 = self.IDToCoord(cur_elem.id_)
found = True
if nid not in heap.pool.keys():
cur_elem = cur_elem.prevID
paths.append([cur_path[::-1], dist])
g_ = heap.pool[removed].g_ + self.getDist((cur_x, cur_y), node[0])
g_ = heap.pool[removed].g_ + self.getDist((cur_x, cur_y), node[0])
coord2 = self.IDToCoord(cur_elem.id_)
f_ = g_ + min(map(lambda x: self.getDist(node[0], x[0]) + x[1], end_points))
if g_ <= heap.pool[nid].g_:
cur_path.append(coord2)
heap.pool[nid] = Node(nid, g_, f_, heap.pool[removed])
heap.pool[nid].g_ = g_
dist += self.getDist(coord1, coord2)
heap.insert(nid)
heap.pool[nid].f_ = g_ + min(map(lambda x: self.getDist(node[0], x[0]) + x[
    1], end_points))
heap.pool[nid].prevID = heap.pool[removed]
heap.insert(nid)
