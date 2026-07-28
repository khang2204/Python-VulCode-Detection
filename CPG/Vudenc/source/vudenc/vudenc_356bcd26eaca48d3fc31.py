def test_parse_magnetlink_lowercase(self):...
"""docstring"""
_, hashed, _ = parse_magnetlink(
    'magnet:?xt=urn:btih:apctqfwnowubxzoidazgaj2ba6fs6juc')
self.assertEqual(hashed, "\x03Å8\x16Íu¨\x1båÈ\x182`'A\x07\x8b/&\x82")
