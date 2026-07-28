def test_bracket_comment(self):...
self.compilation_ok(
    """
if size :over 100K { /* this is a comment
    this is still a comment */ discard /* this is a comment
    */ ;
}
"""
    )
self.representation_is(
    """
if (type: control)
    size (type: test)
        :over
        100K
    discard (type: action)
"""
    )
