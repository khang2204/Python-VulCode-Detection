def test_bad_arg_value(self):...
self.compilation_ko(
    """
if header :isnot "Sent" "me@example.com" {
  stop;
}
""")
