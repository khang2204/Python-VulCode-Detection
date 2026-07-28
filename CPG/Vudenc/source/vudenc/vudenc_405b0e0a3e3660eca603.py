def test_extra_arg(self):...
self.compilation_ko(
    """
if address :is "From" "tim@example.com" "tutu" {
    discard;
}
""")
