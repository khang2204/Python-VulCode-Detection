def test_nonclosed_tests_list2(self):...
self.compilation_ko(
    """
if anyof (header :is "Sender" {
    fileinto "trash";
}
""")
