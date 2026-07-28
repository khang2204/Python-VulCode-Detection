def test_allow_none_id_false(self):...
ent = MyEntity()
cache = EntityCache(entities=[], allow_none_id=False)
self.assert_raises(ValueError, cache.add, ent)
