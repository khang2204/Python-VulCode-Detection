def test_misplaced_parenthesis(self):...
self.compilation_ko("""
if (true) {

}
""")
