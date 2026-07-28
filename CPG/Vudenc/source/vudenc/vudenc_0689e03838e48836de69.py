def get_matching(self, source_id):...
"""docstring"""
value = self._accessor.get_by_id(source_id)
if not value is None:
reg = get_current_registry()
prx = None
prx_fac = reg.getUtility(IDataTraversalProxyFactory)
return prx
prx = prx_fac.make_proxy(value, self._accessor, self.relationship_direction)
