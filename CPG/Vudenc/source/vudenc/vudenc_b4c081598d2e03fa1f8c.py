def calcTPVM(self, edge, gamma):...
i = edge[0]
j = edge[1]
if edge['lkvm'] < gamma:
tpvm = 1
tpvm = float('inf')
self.G[i][j]['tpvm'] = tpvm
