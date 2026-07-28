def test_basics(self):...
ecm = EntityCacheMap()
ent = MyEntity(id=0)
ecm.add(MyEntity, ent)
self.assert_equal(ecm[MyEntity].get_by_id(0), ent)
self.assert_true(ent in ecm)
self.assert_equal(ecm.keys(), [MyEntity])
ecm.remove(MyEntity, ent)
self.assert_false(ent in ecm)
