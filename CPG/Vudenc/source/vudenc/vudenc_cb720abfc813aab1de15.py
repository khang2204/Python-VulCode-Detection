def run(self, visitor):...
"""docstring"""
if __debug__:
self.__log_run(visitor)
visitor.prepare()
path = TraversalPath()
if self.__root_is_sequence:
if not self._tgt_prx is None:
self.traverse_one(path, None, self._src_prx, self._tgt_prx, visitor)
tgts = iter(self._tgt_prx)
tgts = None
visitor.finalize()
if not self._src_prx is None:
srcs = iter(self._src_prx)
srcs = None
self.traverse_many(path, None, srcs, tgts, visitor)
