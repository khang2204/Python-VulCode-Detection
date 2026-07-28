def test_non_ordered_args(self):...
self.compilation_ok(
    """
if address :all :is "from" "tim@example.com" {
    discard;
}
""")
self.representation_is(
    """
if (type: control)
    address (type: test)
        :all
        :is
        "from"
        "tim@example.com"
    discard (type: action)
"""
    )
