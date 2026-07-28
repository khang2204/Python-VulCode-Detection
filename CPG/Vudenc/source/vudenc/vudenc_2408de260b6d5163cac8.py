def test_bad_comparator_value(self):...
self.compilation_ko(
    """
if header :contains :comparator "i;prout" "Subject" "MAKE MONEY FAST" {
  discard;
}
"""
    )
