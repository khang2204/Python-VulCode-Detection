def test_just_one_command(self):...
self.compilation_ok('keep;')
self.representation_is("""
keep (type: action)
""")
