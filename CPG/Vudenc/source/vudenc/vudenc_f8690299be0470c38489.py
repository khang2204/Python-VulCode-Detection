def test_unknown_token(self):...
self.compilation_ko(
    """
if header :is "Sender" "Toto" & header :contains "Cc" "Tata" {
    
}
"""
    )
