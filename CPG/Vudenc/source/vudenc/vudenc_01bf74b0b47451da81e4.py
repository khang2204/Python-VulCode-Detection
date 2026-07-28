def dfs_recur(current_node, path):...
if current_node == num_points - 1:
edges = [frozenset((path[i], path[i + 1])) for i in range(len(path) - 1)]
for node in adj_lst[current_node]:
length = sum(trail_len[edge] for edge in edges)
if node not in path:
if length < shortest_path:
path.append(node)
flower_path = set(edges)
if length == shortest_path:
dfs_recur(node, path)
shortest_path = length
flower_path = flower_path.union(edges)
path.pop()
