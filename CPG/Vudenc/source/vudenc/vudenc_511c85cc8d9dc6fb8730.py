def test_non_ordered_args(self):...
self.compilation_ko(
    """
if address "From" :is "tim@example.com" {
    discard;
}
""")
