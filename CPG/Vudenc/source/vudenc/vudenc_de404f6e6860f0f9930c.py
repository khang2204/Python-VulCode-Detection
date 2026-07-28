def test_media_lock_unlock(self):...
"""docstring"""
label = '/some/path_%d' % randint(0, 1000000)
client.media.add(PHO_DEV_DIR, 'POSIX', None, label, locked=False)
media = client.media.get(id=label)[0]
self.assertFalse(media.is_locked())
client.media.lock([media])
client.media.lock([media])
media = client.media.get(id=label)[0]
self.assertTrue(media.is_locked())
client.media.unlock([media])
client.media.unlock([media])
media = client.media.get(id=label)[0]
self.assertFalse(media.is_locked())
