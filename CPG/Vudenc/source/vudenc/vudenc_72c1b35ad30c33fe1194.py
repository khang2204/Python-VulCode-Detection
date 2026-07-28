def test_empty_not(self):...
self.compilation_ko("""
if not {
    discard;
}
""")
