def test_not_included_extension(self):...
self.compilation_ko(
    """
if header :contains "Subject" "MAKE MONEY FAST" {
  fileinto "spam";
}
"""
    )
