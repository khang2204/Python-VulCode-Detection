def test_multiple_not(self):...
self.compilation_ok("""
if not not not not true {
    stop;
}
""")
self.representation_is(
    """
if (type: control)
    not (type: test)
        not (type: test)
            not (type: test)
                not (type: test)
                    true (type: test)
    stop (type: control)
"""
    )
