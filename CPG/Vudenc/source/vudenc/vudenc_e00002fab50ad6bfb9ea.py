def retrieve(self, filter_expression=None, order_expression=None,...
"""docstring"""
ents = iter(self.__entities)
if not filter_expression is None:
ents = filter_expression(ents)
if not order_expression is None:
ents = iter(order_expression(ents))
if not slice_expression is None:
ents = islice(ents, slice_expression.start, slice_expression.stop)
return ents
