def test_basics(self):...
ent = MyEntity(id=0)
cache = EntityCache(entities=[])
cache.add(ent)
self.assert_true(cache.get_by_id(ent.id) is ent)
self.assert_true(cache.has_id(ent.id))
self.assert_true(cache.get_by_slug(ent.slug) is ent)
self.assert_true(cache.has_slug(ent.slug))
ent1 = MyEntity(id=0)
txt = 'FROBNIC'
ent1.text = txt
cache.replace(ent1)
self.assert_equal(cache.get_by_id(ent.id).text, txt)
self.assert_equal(cache.get_all(), [ent])
self.assert_equal(list(cache.retrieve()), [ent])
cache.remove(ent)
self.assert_is_none(cache.get_by_id(ent.id))
self.assert_is_none(cache.get_by_slug(ent.slug))
