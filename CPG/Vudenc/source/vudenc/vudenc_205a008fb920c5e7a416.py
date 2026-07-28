def test_explicit_comparator(self):...
self.compilation_ok(
    """
if header :contains :comparator "i;octet" "Subject" "MAKE MONEY FAST" {
  discard;
}
"""
    )
self.representation_is(
    """
if (type: control)
    header (type: test)
        "i;octet"
        :contains
        "Subject"
        "MAKE MONEY FAST"
    discard (type: action)
"""
    )
