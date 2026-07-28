def test_misplaced_elsif2(self):...
self.compilation_ko("""
elsif header :is "From" "toto" {

}
""")
