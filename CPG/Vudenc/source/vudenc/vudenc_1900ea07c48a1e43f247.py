def calcWLPVM(self, edge, l):...
i = edge[0]
j = edge[1]
wlpvm = 1 + 1.0 * l / edge['lkvm']
self.G[i][j]['wlpvm'] = wlpvm
