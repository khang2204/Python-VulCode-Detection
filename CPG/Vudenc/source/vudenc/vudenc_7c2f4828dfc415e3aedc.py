def test_parse_magnetlink_uppercase(self):...
"""docstring"""
_, hashed, _ = parse_magnetlink(
    'magnet:?xt=urn:btih:APCTQFWNOWUBXZOIDAZGAJ2BA6FS6JUC')
self.assertEqual(hashed, "\x03Å8\x16Íu¨\x1båÈ\x182`'A\x07\x8b/&\x82")
