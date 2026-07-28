def depict_paths(self, createexpr):...
"""docstring"""
searcher = pathexpr.SearcherNotExists(self, createexpr)
ctx = ds.PathTraversalContext({}, {}, self._root, {}, None, None, None)
rule = self._doc['rules']['ROOT']
ds._traverse(searcher, rule, ctx, self)
return searcher._store
