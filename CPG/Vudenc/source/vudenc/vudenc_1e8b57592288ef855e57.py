def test_nonclosed_block(self):...
self.compilation_ko(
    """
if header :is "Sender" "me@example.com" {
    discard;

""")
