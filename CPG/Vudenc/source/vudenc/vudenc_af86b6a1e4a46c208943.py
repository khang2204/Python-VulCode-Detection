def test_nested_comments(self):...
self.compilation_ko(
    """
/* this is a comment /* with a nested comment inside */
it is allowed by the RFC :p */
"""
    )
