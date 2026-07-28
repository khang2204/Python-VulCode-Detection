def test_true_test(self):...
self.compilation_ok("""
if true {

}
""")
self.representation_is("""
if (type: control)
    true (type: test)
""")
