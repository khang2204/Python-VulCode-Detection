def test_reject_extension(self):...
self.compilation_ok(
    """
require "reject";

if header :contains "subject" "viagra" {
    reject;
}
"""
    )
