def test_filter_order_slice(self):...
ent0 = MyEntity(id=0)
ent1 = MyEntity(id=1)
ent2 = MyEntity(id=2)
cache = EntityCache(entities=[])
cache.add(ent0)
cache.add(ent1)
cache.add(ent2)
filter_expr = EvalFilterExpression(~eq(id=0))
order_expr = EvalOrderExpression(asc('id'))
slice_expr = slice(1, 2)
self.assert_equal(list(cache.retrieve(filter_expression=filter_expr,
    order_expression=order_expr, slice_expression=slice_expr)), [ent2])
