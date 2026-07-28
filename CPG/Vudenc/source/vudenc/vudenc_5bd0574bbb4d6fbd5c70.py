def test_misplaced_comma_in_tests_list(self):...
self.compilation_ko(
    """
if anyof (header :is "Sender" "me@example.com",) {

}
""")
