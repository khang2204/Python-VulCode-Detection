def test_singletest_testlist(self):...
self.compilation_ok("""
if anyof (true) {
    discard;
}
""")
self.representation_is(
    """
if (type: control)
    anyof (type: test)
        true (type: test)
    discard (type: action)
"""
    )
