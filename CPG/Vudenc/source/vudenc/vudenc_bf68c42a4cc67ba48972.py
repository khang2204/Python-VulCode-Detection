def test_missing_semicolon_in_block(self):...
self.compilation_ko("""
if true {
    stop
}
""")
