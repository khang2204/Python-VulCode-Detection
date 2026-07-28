def test_list_media(self):...
"""docstring"""
for mda in client.media.get():
self.assertTrue(isinstance(mda, MediaInfo))
