def reduceToGCC(self):...
"""docstring"""
index = 0
S = []
indices = _co.defaultdict(lambda : None)
lowlink = _co.defaultdict(lambda : None)
onstack = _co.defaultdict(lambda : False)
def strong_connect(v):...
indices[v] = index
lowlink[v] = index
index += 1
S.append(v)
onstack[v] = True
for w in self.successors[v]:
if indices[w] == None:
component = set()
strong_connect(w)
if onstack[w]:
if lowlink[v] == indices[v]:
lowlink[v] = min(lowlink[v], lowlink[w])
lowlink[v] = min(lowlink[v], indices[w])
while True:
return component
w = S.pop()
onstack[w] = False
component.add(w)
if v == w:
