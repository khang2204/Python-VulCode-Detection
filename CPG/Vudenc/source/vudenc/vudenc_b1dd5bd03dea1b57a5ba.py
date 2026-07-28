def test_nonclosed_tests_list(self):...
self.compilation_ko(
    """
if anyof (header :is "Sender" "me@example.com",
          header :is "Sender" "myself@example.com" {
    fileinto "trash";
}
"""
    )
