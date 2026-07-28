def test_invalid_output(self):...
out = list(self.uut.process_output(['1.0|0: Info message\n',
    '2.2|1: Normal message\n', """3.4|2: Major message
"""], 'a/file.py', [
    'original_file_lines_placeholder']))
self.assertEqual(len(out), 3)
self.assertEqual(out[0].origin, 'Lint')
self.assertEqual(out[0].affected_code[0], SourceRange.from_values(
    'a/file.py', 1, 0))
self.assertEqual(out[0].severity, RESULT_SEVERITY.INFO)
self.assertEqual(out[0].message, 'Info message')
self.assertEqual(out[1].affected_code[0], SourceRange.from_values(
    'a/file.py', 2, 2))
self.assertEqual(out[1].severity, RESULT_SEVERITY.NORMAL)
self.assertEqual(out[1].message, 'Normal message')
self.assertEqual(out[2].affected_code[0], SourceRange.from_values(
    'a/file.py', 3, 4))
self.assertEqual(out[2].severity, RESULT_SEVERITY.MAJOR)
self.assertEqual(out[2].message, 'Major message')
