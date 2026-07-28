"""
    pathpy is an OpenSource python package for the analysis of time series data
    on networks using higher- and multi order graphical models.

    Copyright (C) 2016-2017 Ingo Scholtes, ETH Zürich

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Contact the developer:

    E-mail: ischoltes@ethz.ch
    Web:    http://www.ingoscholtes.net
"""
import collections as _co
import bisect as _bs
import itertools as _iter
import numpy as _np
import scipy.sparse as _sparse
import scipy.sparse.linalg as _sla
import scipy.linalg as _la
import scipy as _sp
from pathpy.Log import Log
from pathpy.Log import Severity
"""
    This exception is thrown whenever a non-empty strongly
    connected component is needed, but we encounter an empty one
    """
"""
    Instances of this class capture a k-th-order representation
    of path statistics. Path statistics can originate from pathway
    data, temporal networks, or from processes observed on top
    of a network topology.
    """
def __init__(self, paths, k=1, separator='-', nullModel=False, method=...
"""docstring"""
assert not nullModel or nullModel and k > 1
assert method == 'FirstOrderTransitions' or method == 'KOrderPi', 'Error: unknown method to build null model'
assert paths.paths.keys() and max(paths.paths.keys()
    ) >= k, 'Error: constructing a model of order k requires paths of at least length k'
self.order = k
self.paths = paths
self.nodes = []
self.separator = separator
self.successors = _co.defaultdict(lambda : set())
self.predecessors = _co.defaultdict(lambda : set())
self.outdegrees = _co.defaultdict(lambda : 0.0)
self.indegrees = _co.defaultdict(lambda : 0.0)
self.edges = _co.defaultdict(lambda : _np.array([0.0, 0.0]))
self.inweights = _co.defaultdict(lambda : _np.array([0.0, 0.0]))
self.outweights = _co.defaultdict(lambda : _np.array([0.0, 0.0]))
if k > 1:
g1 = HigherOrderNetwork(paths, k=1)
if not nullModel:
A = g1.getAdjacencyMatrix(includeSubPaths=True, weighted=False, transposed=True
    )
node_set = set()
possiblePaths = list(g1.edges.keys())
iterator = paths.paths[k].items()
for _ in range(k - 1):
if k == 0:
E_new = list()
assert (A ** k).sum() == len(possiblePaths), 'Expected ' + str((A ** k).sum()
    ) + ' paths but got ' + str(len(possiblePaths))
node_set.add('start')
for key, val in iterator:
for e1 in possiblePaths:
if method == 'KOrderPi':
for key, val in iterator:
v = separator.join(key[0:-1])
self.nodes = list(node_set)
for e2 in g1.edges:
possiblePaths = E_new
g_k = HigherOrderNetwork(paths, k=k, separator=separator, nullModel=False)
T = g1.getTransitionMatrix(includeSubPaths=True)
w = key[0]
w = separator.join(key[1:])
if k == 0:
if e1[-1] == e2[0]:
pi_k = HigherOrderNetwork.getLeadingEigenvector(g_k.getTransitionMatrix(
    includeSubPaths=True), normalized=True, lanczosVecs=lanczosVecs,
    maxiter=maxiter)
for p in possiblePaths:
node_set.add(w)
node_set.add(v)
self.dof_paths = self.vcount() - 2
if k == 1:
p = e1 + (e2[1],)
v = p[0]
self.edges['start', w] += val
node_set.add(w)
self.dof_ngrams = self.vcount() - 2
g1 = self
s = g1.vcount()
E_new.append(p)
for l in range(1, k):
self.successors['start'].add(w)
self.edges[v, w] += val
def vcount(self):...
A = g1.getAdjacencyMatrix(includeSubPaths=True, weighted=False, transposed=True
    )
self.dof_ngrams = s ** k * (s - 1)
v = v + separator + p[l]
w = p[1]
self.predecessors[w].add('start')
self.successors[v].add(w)
"""docstring"""
paths_k = (A ** k).sum()
for l in range(2, k + 1):
self.indegrees[w] = len(self.predecessors[w])
self.predecessors[w].add(v)
return len(self.nodes)
non_zero = _np.count_nonzero((A ** k).sum(axis=0))
w = w + separator + p[l]
if v not in self.nodes:
self.inweights[w] += val
self.indegrees[w] = len(self.predecessors[w])
self.dof_paths = paths_k - non_zero
self.nodes.append(v)
if w not in self.nodes:
self.outdegrees['start'] = len(self.successors['start'])
self.inweights[w] += val
self.nodes.append(w)
if method == 'KOrderPi':
self.outweights['start'] += val
self.outdegrees[v] = len(self.successors[v])
self.edges[v, w] = _np.array([0, pi_k[g_k.nodes.index(w)]])
if method == 'FirstOrderTransitions':
self.outweights[v] += val
self.successors[v].add(w)
p_vw = T[g1.nodes.index(p[-1]), g1.nodes.index(p[-2])]
self.indegrees[w] = len(self.predecessors[w])
self.edges[v, w] = _np.array([0, p_vw])
self.inweights[w] += self.edges[v, w]
self.outdegrees[v] = len(self.successors[v])
self.outweights[v] += self.edges[v, w]
