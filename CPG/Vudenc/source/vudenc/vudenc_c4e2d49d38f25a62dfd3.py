def test_string_with_bracket_comment(self):...
self.compilation_ok(
    """
if header :contains "Cc" "/* comment */" {
    discard;
}
""")
self.representation_is(
    """
if (type: control)
    header (type: test)
        :contains
        "Cc"
        "/* comment */"
    discard (type: action)
"""
    )
