def test_custom_regex(self):...
self.uut.output_regex = (
    '(?P<origin>\\w+)\\|(?P<line>\\d+)\\.(?P<column>\\d+)\\|(?P<end_line>\\d+)\\.(?P<end_column>\\d+)\\|(?P<severity>\\w+): (?P<message>.*)'
    )
self.uut.severity_map = {'I': RESULT_SEVERITY.INFO}
out = list(self.uut.process_output(['info_msg|1.0|2.3|I: Info message\n'],
    'a/file.py', ['original_file_lines_placeholder']))
self.assertEqual(len(out), 1)
self.assertEqual(out[0].affected_code[0].start.line, 1)
self.assertEqual(out[0].affected_code[0].start.column, 0)
self.assertEqual(out[0].affected_code[0].end.line, 2)
self.assertEqual(out[0].affected_code[0].end.column, 3)
self.assertEqual(out[0].severity, RESULT_SEVERITY.INFO)
self.assertEqual(out[0].origin, 'Lint (info_msg)')
