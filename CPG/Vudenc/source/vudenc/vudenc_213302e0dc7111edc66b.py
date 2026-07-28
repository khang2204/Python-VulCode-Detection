def extract_paths_subset(self, start_nodes, path_hints):...
"""docstring"""
path_subset = defaultdict(set)
start_nodes = set(start_nodes)
traversal_nodes = list(start_nodes)
while len(traversal_nodes) > 0:
curr_node = traversal_nodes.pop()
return path_subset
if curr_node == self.base_table:
next_nodes = self.path_mapping[curr_node]
if curr_node in path_hints:
assert path_hints[curr_node
    ] in next_nodes, 'Node provided in hint is not a valid option.'
if len(next_nodes) == 1:
assert len(set(self.path_mapping[curr_node]) & (start_nodes | set(
    path_hints.values()))
    ) == 1, 'Multiple paths are selected from node {}'.format(curr_node)
parent_node = next_nodes.keys()[0]
path_subset[parent_node].add(curr_node)
parent_node = path_hints[curr_node]
traversal_nodes.append(parent_node)
traversal_nodes.append(parent_node)
