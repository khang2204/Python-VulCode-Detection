def test_nested_blocks(self):...
self.compilation_ok(
    """
if header :contains "Sender" "example.com" {
  if header :contains "Sender" "me@" {
    discard;
  } elsif header :contains "Sender" "you@" {
    keep;
  }
}
"""
    )
self.representation_is(
    """
if (type: control)
    header (type: test)
        :contains
        "Sender"
        "example.com"
    if (type: control)
        header (type: test)
            :contains
            "Sender"
            "me@"
        discard (type: action)
    elsif (type: control)
        header (type: test)
            :contains
            "Sender"
            "you@"
        keep (type: action)
"""
    )
