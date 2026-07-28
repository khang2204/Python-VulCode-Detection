def get_attribute_proxy(self, attribute):...
"""docstring"""
attr_val = self._get_relation_attribute_value(attribute)
if attr_val is None:
prx = None
if not self._accessor is None:
return prx
acc = self._make_accessor(attribute.attr_type)
acc = None
reg = get_current_registry()
prx_fac = reg.getUtility(IDataTraversalProxyFactory)
prx = prx_fac.make_proxy(attr_val, acc, self.relationship_direction,
    options=self._get_proxy_options(attribute))
