def inp():...
first_line = input().split(' ')
num_points, num_trails = int(first_line[0]), int(first_line[1])
adj_lst = {i: set() for i in range(num_points)}
trail_len = {}
trail_len_duplicate_count = {}
for i in range(num_trails):
trail = input().split(' ')
return num_points, adj_lst, trail_len, trail_len_duplicate_count
node1, node2, length = int(trail[0]), int(trail[1]), int(trail[2])
if node1 != node2:
adj_lst[node1].add(node2)
adj_lst[node2].add(node1)
key = frozenset((node1, node2))
if key in trail_len and length >= trail_len[key]:
trail_len_duplicate_count[key] += 1 if length == trail_len[key] else 0
trail_len[key] = length
trail_len_duplicate_count[key] = 1
