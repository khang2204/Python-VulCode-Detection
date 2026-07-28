def parse_node_strings(self):...
"""docstring"""
if not self['nodes']:
return
nodes = []
if not isinstance(self['nodes'], list):
self['nodes'] = [self['nodes']]
for node in self['nodes']:
idxs = [i for i, m in enumerate(node) if m == ',']
self['nodes'] = nodes
idxs.append(len(node))
start = 0
pos = 0
for idx in idxs:
if pos != len(node):
pos = idx
nodes.append(node[pos + 1:])
reg = node[start:idx]
re.compile(re.escape(reg))
if '[' in reg and ']' not in reg:
nodes.append(reg.lstrip(','))
start = idx
