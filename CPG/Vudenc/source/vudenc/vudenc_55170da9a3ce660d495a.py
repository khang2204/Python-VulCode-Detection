def test_hash_comment(self):...
self.compilation_ok(
    """
if size :over 100k { # this is a comment
    discard;
}
""")
self.representation_is(
    """
if (type: control)
    size (type: test)
        :over
        100k
    discard (type: action)
"""
    )
