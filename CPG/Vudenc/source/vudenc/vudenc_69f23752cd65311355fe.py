def test_misplaced_elsif(self):...
self.compilation_ko("""
elsif true {

}
""")
