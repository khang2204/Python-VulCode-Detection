def test_truefalse_testlist(self):...
self.compilation_ok("""
if anyof(true, false) {
    discard;
}
""")
self.representation_is(
    """
if (type: control)
    anyof (type: test)
        true (type: test)
        false (type: test)
    discard (type: action)
"""
    )
