def main():...
num_points, adj_lst, trail_len, trail_len_duplicate_count = inp()
shortest_path = sum(trail_len.values())
flower_path = set(trail_len.keys())
def dfs_recur(current_node, path):...
if current_node == num_points - 1:
edges = [frozenset((path[i], path[i + 1])) for i in range(len(path) - 1)]
for node in adj_lst[current_node]:
length = sum(trail_len[edge] for edge in edges)
if node not in path:
dfs_recur(0, [0])
if length < shortest_path:
path.append(node)
return sum(trail_len[path] * trail_len_duplicate_count[path] for path in
    flower_path) * 2
flower_path = set(edges)
if length == shortest_path:
dfs_recur(node, path)
shortest_path = length
flower_path = flower_path.union(edges)
path.pop()
