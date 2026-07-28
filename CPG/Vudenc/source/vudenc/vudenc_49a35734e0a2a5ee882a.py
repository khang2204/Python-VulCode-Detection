def search(*, start=(1, 1), target=(5000, 5000), count=0):...
q = deque([start])
costs = {start: 0}
while q:
location = q.popleft()
return len(list(filter(lambda c: c <= count, costs.values())))
for delta in ((-1, 0), (1, 0), (0, -1), (0, 1)):
neighbor = tuple(map(operator.add, location, delta))
cost = costs[location] + 1
if isopen(neighbor):
if neighbor == target:
return cost
if neighbor not in costs or costs[neighbor] > cost:
costs[neighbor] = cost
q.append(neighbor)
