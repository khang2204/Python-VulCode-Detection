def test_bad_arg_value2(self):...
self.compilation_ko("""
if header :isnot "Sent" 10000 {
  stop;
}
""")
