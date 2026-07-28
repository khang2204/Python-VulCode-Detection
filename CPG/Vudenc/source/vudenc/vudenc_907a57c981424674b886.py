def test_missing_semicolon(self):...
self.compilation_ko("""
require ["fileinto"]
""")
